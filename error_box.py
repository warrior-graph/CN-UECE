# Calcula o erro absoluto
def absolute_error(x, x_aprox):
    return abs(x - x_aprox)

# Calcula o erro relativo
def relative_error(abs_error, x_aprox):
    return abs_error / abs(x_aprox)