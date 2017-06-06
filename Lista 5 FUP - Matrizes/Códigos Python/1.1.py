m = []
for i in range(0,6):
	m.append([[], [], []])
for i in range(0,6):
	for j in range(0,3):
		m[i][j] = int(input("Digite o valor da linha %i com a coluna %i: " % (i+1, j+1)))
maior = m[1][1]
menor = m[1][1]
for i in range(0,6):
	for j in range(0,3):
		print (m[i][j], end="")
		if maior < m[i][j]:
			maior = m[i][j]
		if menor > m[i][j]:
			menor = m[i][j]
		print("\n")
print("O maior elemento da matriz é: %i \nE o menor elemento da matriz é: %i" % (maior, menor))
