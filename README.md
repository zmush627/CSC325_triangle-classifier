# CSC325_triangle-classifier

How to run the tests
bash
python -m venv venv
venv\Scripts\activate          # Windows PowerShell
source venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
pytest -v

All tests should pass (11 unit tests and 1 acceptance test).


Class	Example	Expected
Non-positive side (zero)	(0, 4, 5)	Invalid
Non-positive side (negative)	(-3, 4, 5)	Invalid
Triangle inequality fails	(1, 2, 10)	Invalid
Equilateral	(3, 3, 3)	Equilateral
Isosceles, not right	(5, 5, 8)	Isosceles
Scalene, not right	(4, 5, 6)	Scalene
Right scalene	(3, 4, 5)	Right Scalene
Right isosceles (non-integer hypotenuse)	(5, 5, 5*sqrt(2))	Right Isosceles
Boundaries
Boundary	Example	Expected
Side equals 0	(0, 4, 5)	Invalid
Degenerate: two sides sum exactly to the third	(1, 2, 3)	Invalid
Just above degenerate (sum slightly greater than third)	(2, 2, 3)	Isosceles (valid)
Just off a right angle	(3, 4, 5.0001)	Scalene, not Right
Argument order	(5, 3, 4), (4, 5, 3)	Right Scalene


An equilateral triangle has three equal angles that sum to 180 degrees, so each is 60 degrees, never 90 degrees. If every side is s, the Pythagorean theorem would be s^2 + s^2 = s^2, but 2s^2 /= s^2 for any positive s.


test_triangle.py - Copilot was used - Kept - Copilot assisted with the overall bodies for the tests. (all tests failed)

test_triangle.py - Copilot was used - Rejected - Copilot suggested Capitalizing The test results (I did it myself).


ACCEPTANCE CRITERIA

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


AI-use disclosure
GitHub Copilot: used to complete the test bodies in test_triangle.py. Every suggestion was checked against the specification table; the mistakes it made are listed in the review log above. Copilot was not used for test_acceptance.py.
Claude: used for planning and step-by-step guidance, for drafting triangle.py, for drafting the skeleton of test_triangle.py (test names and docstrings).
