#!/usr/bin/python
#-*- coding:utf-8 -*-

#author: Franklyn Seabra Rogério Bezerra
#curso: Ciências da computação, cadeira de Fundamentos de programação
#professor: José Maria Da Silva Monteiro Filho

#questão 2 lista 8
ordem_servicos = []

somaValor = 0.0
maiorValor = 0.0

for i in range(20):
  print("Ordem de Serviço %d" %(i+1))
  numOS = float(input("Digite o número da OS:"))
  data = input("Digite a data: ")
  
  valor = float(input("Digite o valor do Serviço: R$"))
  somaValor += valor
  if valor > maiorValor:
    maiorValor = valor
    
  descricao = input("Digite a descrição:")
  nomeCliente = input("Digite o nome do Cliente")
  
  
  ordem_servico = {"numOS":numOS, "data":data, "valor":valor, "descricao":descricao, "nomeCliente":nomeCliente}
  ordem_servicos.append(ordem_servico)
  
print("A média dos valores dos serviços realizados é R$ %.2f" %(somaValor/20))
print("\nCliente(s) com maior valor:")
for i in range(2):
  if maiorValor == ordem_servicos[i]["valor"]:
    print("Nome: %s" % (ordem_servicos[i]["nomeCliente"]))
    print("Descrição: %s" % (ordem_servicos[i]["descricao"]))
    print("Data: %s" % (ordem_servicos[i]["data"]))