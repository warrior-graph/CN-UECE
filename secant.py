import random
from function_box import f

# Recebe como parâmetro a precisão
def secant(eps):
	# Randomiza os valores das aproximações iniciais x0 e x1
	x0 = random.randrange(1, 10)
	x1 = random.randrange(1, 10)

	# Se o módulo de f(x0) for menor que o erro, d = x0
	if abs(f(x0)) < eps:
		return x0

	# Se o módulo de f(x1) ou o módulo da diferença entre as aproximações x1 e
	# x0 for menor que o erro, d = x1
	if abs(f(x1)) < eps or abs(x1 - x0) < eps:
		return x1

	# Número de iterações k começa por 1 e loop roda até encontrar a raiz d
	k = 1
	while (True):
		# Nova aproximação x2 é calculada a partir da função de iteração do
		# método e arredonda o valor para 5 casas decimais
		x2 = round(x1 - f(x1) / (f(x1) - f(x0)) * (x1 - x0), 5)

		# Se o módulo de f(x2) ou o módulo da diferença entre as aproximações
		# x2 e x1 for menor que o erro, d = x2
		if abs(f(x2)) < eps or abs(x2 - x1) < eps:
			return x2
	
		# Caso raiz não seja encontrada, atualiza os valores das aproximações
		# e incrementa a variável da iteração
		x0 = x1
		x1 = x2
		k += 1