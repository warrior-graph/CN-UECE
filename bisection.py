def bisection(i, j, f, eps=10e-4):
    if f(i) * f(j) > 0:
        print("No root found.")
    else:
        while (j - i) > eps:
            m = (i + j) * 0.5
            
            if f(m) == 0:
                return m
            elif f(i) * f(m) < 0:
                j = m
            else:
                i = m
        
        return m
