'''1.13. Criar um programa que leia uma matriz ANxN (N < 10) e verifique (informe) se tal
matriz é ou não simétrica (At = A).
autor: Franklyn Seabra Rogério Bezerra
1° Semestre Ciências da Computação

'''
c = int(input("Digite a quantidade de colunas da matriz: "))
l = int(input("Digite a quantidade de linhas da matriz: "))
m = []
t = []
simetrica = False
teste = 0
if l < 10 and c < 10:
	for i in range(l):
		m.append([])
		for j in range(c):
			m[i].append(int(input("Digite o valor da linha %i com a coluna %i da matriz: " %(i+1,j+1) )))

	for i in range(c):
		t.append([])
		for j in range(l):
			t[i].append(int(m[j][i]))

	for i in range(c):
		t.append([])
		for j in range(l):
			if t[i][j] == m[i][j]:
				teste = teste + 1
	if teste == c*l:
		simetrica = True
	print("A matriz é simetrica?", simetrica)
else:
	print("A linha e a coluna tem que ser menores que 10")