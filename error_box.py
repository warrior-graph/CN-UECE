# Calcula o erro relativo por iteração
def relative_error(x, x_aprox):
    return abs(x - x_aprox) / abs(x_aprox)

# Calcula o erro relativo para cada iteração de um método, recebendo uma lista
# com todos as aproximações de d calculadas como parâmetro
def re_per_method(iter_values):
    re_values = []

    for x_aprox in iter_values:
        re_values.append(relative_error(iter_values[-1], x_aprox))

    return re_values