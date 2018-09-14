# Calcula o erro relativo dado um valor d e um d aproximado
def relative_error(d, d_aprox):
    return abs((d - d_aprox) / (d_aprox))


# Recebe uma lista com as aproximações de d calculadas em um método e calcula os
# erros relativos por iteração, setando d como o último valor calculado no método
def re_per_method(iter_values):
    re_values = []

    for d_aprox in iter_values:
        re_values.append(relative_error(iter_values[-1], d_aprox))

    return re_values
