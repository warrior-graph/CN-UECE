import math

def f(d, a = 1):
    return a * math.exp(d) - 4 * d**2

def f_derived(d, a = 1):
	return a * math.exp(d) - 8 * d

def newton_raphson (f, e): 
	if(0.5 < e):
		return f(0.5)
	else:
		aux = 0.5
		k = 1
		while(k != 1000):
			x = aux - (f(0.5)/f_derived(0.5))
			if(abs(x - aux) > e):
				aux = x
				k = k + 1
			else: 
				return f(x)	
