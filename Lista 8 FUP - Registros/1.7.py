#!/usr/bin/python
#-*- coding:utf-8 -*-

#author: Franklyn Seabra Rogério Bezerra
#curso: Ciências da computação, cadeira de Fundamentos de programação
#professor: José Maria Da Silva Monteiro Filho

#questão 7 lista 8 Registros
propinas = []
condi = 1
maiorPropPartido = 0
i = 0
while condi != 0:
  print("Propina %d" %(i+1))
  dataPag = input("Digite a data de pagamento:")
  valor = float(input("Digite o valor do beneficiamento: R$"))
  descricao = input("Digite a descrição da obra:")
  nome = input("Digite o nome do beneficiado:")
  sigla = input("Digite a sigla do partido:")

  propina = {"dataPag":dataPag, "valor":valor, "descricao":descricao, "nome":nome, "sigla":sigla}
  propinas.append(propina)
  
  
  condi = int(input("\nDigite 0 para sair do programa.\nDigite qualquer outro valor para continuar\n-->"))
  i += 1
#print("\n", propinas)

partidos = {}
for i in propinas:
  if i["sigla"] in partidos:
    partidos[i["sigla"]] += i["valor"]  
  else:
    partidos[i["sigla"]] = 0
    partidos[i["sigla"]] = i["valor"]
for chave in partidos:
  if partidos[chave] > maiorPropPartido:
    maiorPropPartido = partidos[chave]
    maior = chave
print("O partido que recebeu maior beneficiamento foi o %s com R$%.2f" %(maior, maiorPropPartido))