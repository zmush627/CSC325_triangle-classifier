import math
 
REL_TOL = 1e-9
 
 
def is_valid_triangle(a, b, c) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    x, y, z = sorted((a, b, c))
    return x + y > z
 
 
def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"
 
    ab = math.isclose(a, b, rel_tol=REL_TOL)
    bc = math.isclose(b, c, rel_tol=REL_TOL)
    ac = math.isclose(a, c, rel_tol=REL_TOL)
 
    if ab and bc:
        shape = "Equilateral"
    elif ab or bc or ac:
        shape = "Isosceles"
    else:
        shape = "Scalene"
 
    x, y, z = sorted((a, b, c))
    if math.isclose(x * x + y * y, z * z, rel_tol=REL_TOL):
        return "Right " + shape
 
    return shape
 