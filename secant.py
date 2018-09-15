from function_box import f

# Método da Secante
# Recebe como parâmetros os valores do intervalo (d0, d1), que funcionam como
# chutes iniciais, o valor da precisão (eps), a amplitude (amp) e a função f


def secant(d0, d1, eps, amp, func=f):
    # Inicializa a lista onde serão salvas as aproximações de d e o módulo
    # de d1-d0 a cada iteração
    iter_values = []

    # Se o módulo de f(d0) for menor que o erro, d = d0
    if abs(func(d0, amp)) < eps:
        iter_values.append((d0, abs(d1 - d0)))
        return iter_values

    # Se o módulo de f(d1) ou o módulo da diferença entre as aproximações d1 e
    # d0 for menor que o erro, d = d1
    if abs(func(d1, amp)) < eps or abs(d1 - d0) < eps:
        iter_values.append((d1, abs(d1 - d0)))
        return iter_values

    # Número de iterações vai de 1 a 1000 ou até encontrar a raiz d
    for _ in range(1, 1001):
        # Aproximação d2 é calculada a partir da função de iteração do método
        d2 = d1 - func(d1, amp) / (func(d1, amp) - func(d0, amp)) * (d1 - d0)
        iter_values.append((d2, abs(d2 - d1)))

        # Se o módulo de f(d2) ou o módulo da diferença entre as aproximações
        # d2 e d1 for menor que o erro, d = d2
        if abs(func(d2, amp)) < eps or abs(d2 - d1) < eps:
            return iter_values

        # Caso raiz não seja encontrada, atualiza os valores das aproximações
        d0 = d1
        d1 = d2
