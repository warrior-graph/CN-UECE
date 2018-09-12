from function_box import f

# Recebe como parâmetro o valore de amplitude


def isolation(amp):
    # Número de iterações k vai de 0 a 999 ou até encontrar o intervalo
    for k in range(0, 1001):
                # Se o produto de f(k+1, amp) por f(k, amp) for menor que 0,
        # retorna os valores de k e k+1 como intervalo
        if f(k+1, amp) * f(k, amp) < 0:
            return (k, k+1)
        # Se o produto de f(-k+1, amp) por f(-k, amp) for menor que 0,
        # retorna os valores de -(k+1) e -k como intervalo
        elif f(-(k+1), amp) * f(-k, amp) < 0:
            return (-(k+1), -k)
