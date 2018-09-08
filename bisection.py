from function_box import f

# Recebe como parâmetros os valores do intervalo (a, b) e da precisão
def bisection(a, b, eps, func=f):
    # Se a amplitude do intervalo atinge a precisão requerida, d = média(a, b)
    if (b - a) < eps:
        return (a + b) * 0.5

    # M recebe f(a), sendo a o do intervalo inicial
    M = f(a)

    # Número de iterações k vai de 1 a 1000 ou até encontrar a raiz d
    for k in range(1, 1001):
        # A aproximação x recebe a média da soma de a e b
        x = (a + b) * 0.5

        # Se a multiplicação de M por f(x) for maior que zero, atualiza-se
        # o valor de a
        if (M * func(x)) > 0:
            a = x
            # Se a diferença entre b e a for menor que o erro, ou seja, se a
            # amplitude do intervalo atinge a precisão requerida,
            # d = média(a, b)
            if (b - a) < eps:
                return (a + b) * 0.5
        # Se o resultado da multiplicação não for maior que zero, atualiza-se b
        # e passa-se para a próxima iteração
        else:
            b = x
