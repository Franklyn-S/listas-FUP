#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Esse código cria uma matriz 4x4, onde os valores são escolhidos pelo usuário
e após isso mostra a sua diagonal secundaria

Autor: Franklyn Seabra
Cursando Ciências da computação no 1º semestre
'''
#Cria uma lista para a matriz e uma lista que irá conter a diagonal
m=[]
diagonalS=[0,0,0,0]

#preenche a matriz com os valores digitados pelo usuário
for i in range(0,4):
	m.append([])
	for j in range(0,4):
		m[i].append(int(input("Digite o valor da linha %i com a coluna %i: " % (i+1,j+1))))

#imprime a matriz
print("***Matriz***")
for k in range(0,4):
	print(m[k])

#coloca os valores da diagonal da matriz secundaria(ao contrário) na lista diagonalS
print("***Diagonal Secundária***")
for i in range(0,4):
	for j in range(0,4):
		if i+j == 3:
			diagonalS[j] = m[i][j]
#inverte a diagonal secundária e a imprime
print("Os valores da diagonal secundária são: ")
diagonalS.reverse()
print(diagonalS)
	