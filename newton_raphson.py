from function_box import f, f_derived

# Recebe como parâmetros o valor da aproximação inicial e a precisão


def newton_raphson(d0, eps, amp, func=f, func_derived=f_derived):
    # Inicializa a lista onde serão salvas as aproximações de d
    iter_values = []

    # Se o módulo de f(d0) for menor que o erro, d = d0
    if abs(func(d0, amp)) < eps:
        iter_values.append(d0)
        return iter_values

    # Inicializa dw com o valor da aproximação inicial
    dw = d0

    # Número de iterações k vai de 1 a 1000 ou até encontrar a raiz d
    for _ in range(1, 1001):
        # Nova aproximação x1 é calculada a partir da função de iteração do
        # método com FL

        # Se o módulo de func'(x0) for maior que o erro, usa-se FL = func'(x0) e
        # atualiza o valor de xw
        if abs(func_derived(d0, amp)) > eps:
            d1 = d0 - func(d0, amp)/func_derived(d0, amp)
            dw = d0
        # Senão, usa-se FL = func'(xw)
        else:
            d1 = d0 - func(d0, amp)/func_derived(dw, amp)

        # Adiciona o valor no final da lista de aproximações calculadas
        iter_values.append(d1)

        # Se o módulo de func(x1) ou o módulo da diferença entre as aproximações
        # x1 e x0 for menor que o erro, d = x1 = último valor salvo na lista
        if abs(func(d1, amp)) < eps or abs(d1 - d0) < eps:
            return iter_values

        # Caso a raiz não seja encontrada, atualiza o valor da aproximação x0
        d0 = d1
