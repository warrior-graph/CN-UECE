# Calcula o erro relativo por iteração
def relative_error(d, d_aprox):
    return abs((d - d_aprox) /(d_aprox))


# Calcula o erro relativo para cada iteração de um método, recebendo uma lista
# com todos as aproximações de d calculadas como parâmetro
def re_per_method(iter_values):
    re_values = []

    for d_aprox in iter_values:
        re_values.append(relative_error(iter_values[-1], d_aprox))

    return re_values
