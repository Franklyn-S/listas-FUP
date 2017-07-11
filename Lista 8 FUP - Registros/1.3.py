#!/usr/bin/python
#-*- coding:utf-8 -*-

#author: Franklyn Seabra Rogério Bezerra
#curso: Ciências da computação, cadeira de Fundamentos de programação
#professor: José Maria Da Silva Monteiro Filho

#questão 3 lista 8 Registros
produtos = []

for i in range(10):
  print("Produto %d" %(i+1))
  codigo = int(input("Digite o código do produto:"))
  descricao = input("Digite a descrição:")
  valor = float(input("Digite o valor do produto: R$"))
  quantidade = int(input("Digite a quantidade desse produto:"))

  produto = {"codigo":codigo, "descricao":descricao, "valor":valor, "quantidade":quantidade}
  produtos.append(produto)
  
print(produtos)

print("\n")

for i in range(10):
  for j in range(10):
    aux = produtos[i]
    if produtos[i]["codigo"] < produtos[j]["codigo"]:
      produtos[i] = produtos[j]
      produtos[j] = aux
print(produtos)