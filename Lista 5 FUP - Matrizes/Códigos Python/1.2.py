#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Esse código cria uma matriz 4x4, onde os valores são escolhidos pelo usuário
e após isso mostra a sua diagonal principal

Autor: Franklyn Seabra
Cursando Ciências da computação no 1º semestre
'''
#Cria uma lista para a matriz e uma lista que irá conter a diagonal
m = []
diagonalP = [0,0,0,0]

#preenche a matriz com os valores digitados pelo usuário
for i in range(0,4):
	m.append([])
	for j in range(0,4):
		m[i].append(int(input("Digite a valor da linha %i com a coluna %i: " % (i+1, j+1))))

#imprime a lista		
for k in range(0,4):
	print(m[k])

#Coloca os valores da Diagonal da matriz na lista DiagonalP
for i in range(0,4):
	for j in range(0,4):
		if i == j:
			diagonalP[i] = m[i][j]
#imprime a diagonal principal
print("Os valores da diagonal principal são:")
print (diagonalP)