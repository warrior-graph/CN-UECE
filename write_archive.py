from error_box import re_per_method
# Recebe como argumento uma lista com os dados a serem plotados
def write_data(iter_values, file_name):
	re_values = (iter_values)
	plot_data = []
	for (i, j) in zip(iter_values, re_values):
		plot_data.append((i, j))
	# Abre ou cria o arquivo se ele não existir
	File = open(file_name, "w")
	for i, j in plot_data:
		# Escreve cada tupla da lista como uma linha do arquivo
		File.write(str(i) + " " + str(j) + "\n")
	File.close()
	

