import math

from isolation import isolation
from function_box import f, f_derived
from bisection import bisection
from secant import secant
from newton_raphson import newton_raphson
from write_archive import write_data

def main():
	n = int(input())
						    
	for k in range(0, n):
		amp = float(input())
		eps = float(input())
		(a, b) = isolation(amp)
		print('\nIsolation: ', (a, b))
		bisection_data = bisection(a, b, eps)
		write_data(bisection_data, "Bisection")
		print('Bissection: ', round(bisection_data[-1], 4))
		newton_raphson_data = newton_raphson((a + b) * 0.5, eps)
		write_data(newton_raphson_data, "Newton-Raphson")
		print('Newton-Raphson: ',round(newton_raphson_data[-1], 4))
		secant_data = secant(a, b, eps)
		write_data(secant_data, "Secant")
		print('Secant: ',round(secant_data[-1], 4))


if __name__ == '__main__':
    main()
