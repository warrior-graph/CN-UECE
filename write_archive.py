# Recebe como argumento uma lista com os dados a serem plotados
def write_data(intervals, file_name):
	# Abre ou cria o arquivo se ele não existir
	File = open(file_name, "w")
	for i, j in intervals:
		# Escreve cada tupla da lista como uma linha do arquivo
		File.write(str(i) + " " + str(j) + "\n")
	

