"""
--------------------------------------------------------------------------------
ACCEPTANCE CRITERIA
--------------------------------------------------------------------------------
AC1 — Valid triangle classification:
    Given three positive numbers where the sum of any two sides is strictly
    greater than the third, classify_triangle() returns "Equilateral",
    "Isosceles", or "Scalene" (possibly prefixed with "Right ").

AC2 — Invalid triangle handling:
    Given inputs that fail the triangle inequality (a+b<=c OR b+c<=a OR
    a+c<=b), or any side <= 0, classify_triangle() returns the exact string
    "Invalid" and does NOT raise.

AC3 — Right-angle flagging:
    Given a valid triangle whose sides satisfy the Pythagorean theorem within
    rel_tol=1e-9 on the largest side, the returned string begins with "Right "
    (i.e. "Right Scalene" or "Right Isosceles"). Otherwise it does not.
--------------------------------------------------------------------------------
"""

import math

import pytest

from triangle import classify_triangle, is_valid_triangle



class TestValidTriangleClassification:
    """AC1: valid inputs yield the correct shape word."""

    def test_equilateral(self):
        assert classify_triangle(5, 5, 5) == "Equilateral"

    def test_isosceles(self):
        assert classify_triangle(5, 5, 8) == "Isosceles"

    def test_scalene(self):
        assert classify_triangle(3, 4, 6) == "Scalene"

    def test_order_independence(self):
        """Side order must not change the classification."""
        assert classify_triangle(6, 3, 4) == classify_triangle(3, 4, 6) == "Scalene"
        assert classify_triangle(8, 5, 5) == "Isosceles"
        assert classify_triangle(5, 5, 5) == "Equilateral"



class TestInvalidTriangleHandling:
    """AC2: invalid inputs return exactly the string 'Invalid'; never raise."""

    @pytest.mark.parametrize("a,b,c", [
        (1, 2, 3),      # degenerate: 1+2 == 3
        (1, 2, 10),     # 1+2 < 10
        (0, 5, 5),      # zero side
        (-3, 4, 5),     # negative side
    ])
    def test_returns_invalid_string_not_exception(self, a, b, c):
        result = classify_triangle(a, b, c)   # must not raise
        assert result == "Invalid"

    @pytest.mark.parametrize("a,b,c", [
        (1, 2, 3),
        (0, 5, 5),
        (-3, 4, 5),
    ])
    def test_is_valid_triangle_agrees(self, a, b, c):
        assert is_valid_triangle(a, b, c) is False
        assert classify_triangle(a, b, c) == "Invalid"



class TestRightAngleFlagging:
    """AC3: right triangles get a 'Right ' prefix; others do not."""

    def test_classic_3_4_5(self):
        assert classify_triangle(3, 4, 5) == "Right Scalene"

    def test_right_isosceles(self):
        assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"

    def test_hypotenuse_detected_regardless_of_argument_order(self):
        """Right angle detected even when hypotenuse is not the last argument."""
        assert classify_triangle(5, 3, 4) == "Right Scalene"
        assert classify_triangle(4, 5, 3) == "Right Scalene"
        assert classify_triangle(5, 4, 3) == "Right Scalene"

    def test_non_right_triangles_are_not_flagged(self):
        for sides in [(5, 5, 5), (5, 5, 8), (3, 4, 6)]:
            assert not classify_triangle(*sides).startswith("Right ")

    def test_near_right_triangle_is_not_flagged(self):
        """(3, 4, 5.0001) is close to right but must NOT be flagged."""
        assert classify_triangle(3, 4, 5.0001) == "Scalene"



def test_end_to_end_customer_scenarios():
    """
    Simulates the studio workflow: three customers, three outcomes.
    Verifies the full contract in one shot.
    """
    r1 = classify_triangle(3, 4, 5)
    assert r1 == "Right Scalene"
    assert r1.startswith("Right ")

    r2 = classify_triangle(2, 3, 100)
    assert r2 == "Invalid"

    r3 = classify_triangle(7, 7, 7)
    assert r3 == "Equilateral"
    assert not r3.startswith("Right ")



if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))