import math

from isolation import isolation
from function_box import f, f_derived
from bisection import bisection
from secant import secant
from newton_raphson import newton_raphson

def main():
    n = int(input())
    
    for k in range(0, n):
        amp = float(input())
        eps = float(input())
        (a, b) = isolation(amp)
        print('\nIsolation: ', (a, b))
        print('Bissection: ', round(bisection(a, b, eps), 4))
        print('Newton-Raphson: ',round(newton_raphson((a + b) / 2, eps), 4))
        print('Secant: ',round(secant(a, b, eps), 4))


if __name__ == '__main__':
    main()
