#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Esse código cria uma matriz 4x4, onde os valores são escolhidos pelo usuário
e após isso mostra a todos os valores menos o da sua diagonal principal
Autor: Franklyn Seabra
Cursando Ciências da computação no 1º semestre
'''
#Cria uma lista para a matriz e uma lista que irá todos os valores exceto conter a diagonal
m=[]
lista=[0,0,0,0,0,0,0,0,0,0,0,0]

#preenche a matriz com os valores digitados pelo usuário
for i in range(0,4):
	m.append([])
	for j in range(0,4):
		m[i].append(int(input("Digite o valor da linha %i com a coluna %i: " % (i+1,j+1))))

#imprime a matriz
print("***Matriz***")
for k in range(0,4):
	print(m[k])

#coloca os valores da matriz (exceto os valores da sua diagonal principal) na lista chamada lista
print("***Todos os valores exceto os da diagonal principal***")
aux = 0
for i in range(0,4):
	for j in range(0,4):
		if i != j:
			lista[aux] = m[i][j]
			aux = aux + 1

#imprime os valores da matriz (exceto os valores da sua diagonal principal)
print(lista)