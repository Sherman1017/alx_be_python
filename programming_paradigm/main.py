import sys
from robust_division_calculator import safe_divide

if len(sys.argv) != 3:
    print("Usage: python main.py <numerator> <denominator>")
else:
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    result = safe_divide(numerator, denominator)
    print(result)
