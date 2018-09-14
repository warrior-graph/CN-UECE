from function_box import f

# Encontra um intervalo (a, b) onde exista pelo menos uma raiz de f(d)


def isolation(amp):
    # Valor de k vai de 0 a 1000 ou até encontrar um intervalo válido
    for k in range(0, 1001):
        # Se o produto de f(k+1, amp) por f(k, amp) for menor que 0,
        # retorna os valores de k e k+1 como intervalo
        if f(k+1, amp) * f(k, amp) < 0:
            return (k, k+1)

        # Se o produto de f(-k+1, amp) por f(-k, amp) for menor que 0,
        # retorna os valores de -(k+1) e -k como intervalo
        elif f(-(k+1), amp) * f(-k, amp) < 0:
            return (-(k+1), -k)
