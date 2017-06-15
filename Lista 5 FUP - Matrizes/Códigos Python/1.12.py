'''1.12. Criar um programa que leia uma matriz ANxN (N < 10) e calcule a respectiva matriz
transposta At.
autor: Franklyn Seabra Rogério Bezerra
1° Semestre Ciências da Computação

'''
c = int(input("Digite a quantidade de colunas da matriz: "))
l = int(input("Digite a quantidade de linhas da matriz: "))
m = []
t = []

if l < 10 and c < 10:
	for i in range(l):
		m.append([])
		for j in range(c):
			m[i].append(int(input("Digite o valor da linha %i com a coluna %i da matriz: " %(i+1,j+1) )))

	for i in range(c):
		t.append([])
		for j in range(l):
			t[i].append(int(m[j][i]))

	for k in range(c):
		print(t[k])
else:
	print("A linha e a coluna tem que ser menores que 10")