import math
import random
from function_box import *

def newton_raphson(x0, eps):
	if abs(f(x0)) < eps:
		return x0
	
	k = 1
	xw = x0
	while k != 1000:
		if abs(f_derived(x0)) > eps:
			x1 = round(x0 - f(x0)/f_derived(x0), 5)
			xw = x0
		elif abs(f_derived(xw)) > eps:
			x1 = round(x0 - f(x0)/f_derived(xw), 5)
		else:
			print("Impossível aplicar método usando FL.")
			return

		if abs(f(x1)) < eps or abs(x1 - x0) < eps:
			return x1

		x0 = x1
		k += 1