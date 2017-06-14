A = []
B = []
C = []

for i in range(0,3):
	A.append([])
	for j in range(0,2):
		A[i].append(int(input("Digite o valor da linha %i com a coluna %i da matriz A: " % (i+1, j+1) )))

for j in range(0,2):
	B.append([])
	for k in range(0,5):
		B[j].append(int(input("Digite o valor da linha %i com a coluna %i da matriz B: " % (j+1, k+1) )))

#calcula a matriz A[3][2]*B[2][5] = C[3][5]
for i in range(0,3):
	C.append([])
	for k in range(0,5):
		soma = 0
		for j in range(0,2):
			soma = soma + (A[i][j] * B[j][k])
		C[i].append(soma)

#printa as matrizes
print("***Matriz A***")
for i in range(3):
	print(A[i])

print("***Matriz B***")
for i in range(2):
	print(B[i])

print("***Matriz C***")
for i in range(3):
	print(C[i])
