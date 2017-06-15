'''1.15. Uma matriz quadrada inteira é chamada de quadrado mágico se as somas dos
elementos de cada linha, coluna, e das diagonais principal e secundária são iguais.
Escreva um programa que leia uma matriz A3x3 e exiba uma mensagem na tela dizendo
se ela é ou não um quadrado mágico.
autor do programa: Franklyn Seabra Rogério Bezerra
1° semestre Ciências da Computação - UFC'''
m = []
diagonalP = []
diagonalS = []
linha = []
coluna = []
quadrado = False

#coloca valores na lista coluna
for i in range(3):
	coluna.append(0)

# Usuário atribui valores a matriz e a medida que ele faz isso vai colocando a 
# soma dos valores das linhas, colunas, diagonal principal e secundária nas
# respectivas listas
print("\nDigite os valores da matriz:")
for i in range(3):
	m.append([])
	soma = 0
	for j in range(3):
		m[i].append(int(input("Digite o valor da linha %i com a coluna %i: " %(i+1,j+1) )))
		soma = soma + m[i][j]
		if i == j:
			diagonalP.append(m[i][j])
		if i+j == 2:
			diagonalS.append(m[i][j])
		coluna[j] = coluna[j] + m[i][j]
	linha.append(soma)
soma_diagP = 0
soma_diagS = 0
for i in range(3):
	soma_diagP = soma_diagP + diagonalP[i]
	soma_diagS = soma_diagS + diagonalS[i]
for i in range(3):
	if soma_diagS == soma_diagP and soma_diagS == coluna[i] and soma_diagS == linha[i]:
		quadrado = True
if quadrado == True:
	print("A matriz é quadrado perfeito!")
else:
	print("A matriz NÃO é quadrado perfeito!")
	
