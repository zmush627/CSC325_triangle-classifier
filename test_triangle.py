import math

import pytest

from triangle import classify_triangle, is_valid_triangle

def test_invalid_zero_side():
    """classify_triangle with one side equal to 0, e.g. (0, 4, 5)."""
    assert classify_triangle(0, 4, 5) == "invalid"

def test_invalid_negative_side():
    """classify_triangle with one negative side, e.g. (-3, 4, 5)."""
    assert classify_triangle(-3, 4, 5) == "invalid"

def test_invalid_triangle_inequality_fails():
    """classify_triangle where one side is far too long, e.g. (1, 2, 10)."""
    assert classify_triangle(1, 2, 10) == "invalid"


def test_degenerate_triangle_is_invalid():
    """Boundary: two sides sum exactly to the third, (1, 2, 3).
    Check both classify_triangle and is_valid_triangle."""
    assert is_valid_triangle(1, 2, 3) == False
    assert classify_triangle(1, 2, 3) == "invalid"


def test_equilateral():
    """classify_triangle with all three sides equal, e.g. (3, 3, 3)."""
    assert classify_triangle(3, 3, 3) == "equilateral"


def test_isosceles():
    """classify_triangle with exactly two equal sides, e.g. (5, 5, 8)."""
    assert classify_triangle(5, 5, 8) == "isosceles"

def test_scalene():
    """classify_triangle with all sides different and not a right triangle,
    e.g. (4, 5, 6)."""
    assert classify_triangle(4, 5, 6) == "scalene"


def test_right_scalene():
    """classify_triangle for the 3-4-5 right triangle."""
    assert classify_triangle(3, 4, 5) == "right"


def test_right_isosceles_non_integer_sides():
    """classify_triangle with legs 5 and 5 and hypotenuse 5 * math.sqrt(2).
    This is a float, so watch for any == on floats in the suggestion."""
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "right"


def test_argument_order_does_not_matter():
    """The 3-4-5 triangle given in different orders, e.g. (5, 3, 4)
    and (4, 5, 3), should classify the same way as (3, 4, 5)."""
    assert classify_triangle(5, 3, 4) == "right"
    assert classify_triangle(4, 5, 3) == "right"


def test_near_right_triangle_is_not_right():
    """Sides (3, 4, 5.0001) are close to right but should not be flagged."""
    assert classify_triangle(3, 4, 5.0001) == "scalene"