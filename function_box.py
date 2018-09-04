import math

def f(d, a = 1):
    return a * math.exp(d) - 4 * d**2

def f_derived(d, a = 1):
	return a * math.exp(d) - 8 * d    
