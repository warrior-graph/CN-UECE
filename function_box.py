import math

def f(d, amp = 1):
    return amp * math.exp(d) - 4 * d**2

def f_derived(d, amp = 1):
	return amp * math.exp(d) - 8 * d    
