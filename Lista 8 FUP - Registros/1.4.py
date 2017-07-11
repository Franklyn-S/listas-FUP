#!/usr/bin/python
#-*- coding:utf-8 -*-

#author: Franklyn Seabra Rogério Bezerra
#curso: Ciências da computação, cadeira de Fundamentos de programação
#professor: José Maria Da Silva Monteiro Filho

#questão 4 lista 8 Registros
contas = []
totalJuros = 0
somav = 0
somap = 0
for i in range(2):
  print("Conta %d" %(i+1))
  numDoc = int(input("Digite o número do documento:"))
  codCliente = input("Digite o código do Cliente:")
  dataVenc = input("Digite a data de vencimento:")
  dataPag = input("Digite a data de pagamento:")
  valor = float(input("Digite o valor da conta: R$"))

  conta = {"numDoc":numDoc, "codCliente":codCliente, "dataVenc":dataVenc, "dataPag":dataPag, "valor":valor}
  contas.append(conta)
print(contas)



for i in range(15):
  dataVencimento = contas[i]["dataVenc"].split("/")
  dataPagamento = contas[i]["dataPag"].split("/")
  anop = dataPagamento[2]
  anov = dataVencimento[2]
  mesp = dataPagamento[1]
  mesv = dataVencimento[1]
  diap = dataPagamento[0]
  diav = dataVencimento[0]
  somap = int(diap) + (int(mesp)-1)*30 + int(anop)*365
  somav = int(diav) + (int(mesv)-1)*30 + int(anov)*365
  if somap > somav:
    juros = contas[i]["valor"]*0.02
    totalJuros += (somap-somav)*juros
print("O total de juros é R$%.2f" % (totalJuros))
  
        