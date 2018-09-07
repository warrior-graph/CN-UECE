import math

from function_box import f
from bisection import bisection
from secant import secant
from newton_raphson import newton_raphson

def main():
    print(bisection(0, 1, f))
    print(round(bisection(0, 1, f), 3))
    print(round(newton_raphson(0.0001), 3))
if __name__ == '__main__':
    main()
