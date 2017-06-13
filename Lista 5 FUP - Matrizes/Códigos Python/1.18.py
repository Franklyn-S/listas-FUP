#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Esse código cria uma matriz 3x3, onde os valores são escolhidos pelo usuário
e após isso a mostra virada 270° no sentido horário
Autor: Franklyn Seabra
Cursando Ciências da computação no 1º semestre
'''
#Cria uma lista para a matriz
m=[]

#preenche a matriz com os valores digitados pelo usuário
for i in range(0,3):
    m.append([])
    for j in range(0,3):
        m[i].append(int(input("Digite o valor da linha %i com a coluna %i: " % (i+1,j+1))))

#imprime a matriz original
print("***Matriz***")
for k in range(0,3):
    print(m[k])

#imprime a matriz virada
print("***Matriz Virada***")
for j in range(2,-1,-1):
    print("[", end="")
    for i in range(0,3):
        if i != 2:
            print(m[i][j], end=", ")
        else:
            print(m[i][j], end="]\n")