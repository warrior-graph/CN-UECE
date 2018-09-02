import math

from function_box import f
from bisection import bisection
from secant import secant
from newton_raphson import newton_raphson

def main():
    print(round(bisection(-1, 5, f), 3))

if __name__ == '__main__':
    main()
