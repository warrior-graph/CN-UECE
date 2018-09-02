import math

from bisection import bisection
from secant import secant
from newton_Raphson import newton_Raphson

def f(d, a = 1):
    return a * math.exp(d) - 4 * d**2

def main():
    print(round(bisection(-1, 5, f), 3))

if __name__ == '__main__':
    main()
