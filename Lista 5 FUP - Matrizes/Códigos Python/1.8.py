matriz = []
vetor = []

for i in range(0,3):
	# cria as linhas da matriz
	matriz.append([]) 
	soma = 0
	# cria as colunas da matriz perguntando e inserindo os elementos
	for j in range(0,5):
		matriz[i].append(int(input("Digite o valor da linha %i com a coluna %i: " % (i+1, j+1) )))
		soma = soma + matriz[i][j]
	vetor.append(soma)
print(vetor)