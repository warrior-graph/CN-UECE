import math


def f(d, a = 1):
    return a * math.exp(d) - 4 * d**2


def bisection(i, j, f, eps=10e-4):
    if f(i) * f(j) > 0:
        print("No root found.")
    else:
        while (j - i) * 0.5 > eps:
            m = (i + j) * 0.5
            if f(m) == 0:
                return m
            elif f(i) * f(m) < 0:
                j = m
            else:
                i = m
        
        return m

def secant ():
	pass

def newton_Raphson (): 
	pass

def main():
    print(round(bisection(-1, 5, f), 3))

if __name__ == '__main__':
    main()
