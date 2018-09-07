import math
from function_box import *

def newton_raphson (e): 
	if(0.5 < e):
		return f(0.5)
	else:
		aux = 0.5
		k = 1
		while(k != 1000):
			x = aux - (f(aux)/f_derived(aux))
			if(abs(x - aux) > e and abs(f(x)) > e):
				aux = x
				k = k + 1
			else: 
				return x	
