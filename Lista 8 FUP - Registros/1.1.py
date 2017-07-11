#!/usr/bin/python
#-*- coding:utf-8 -*-

#author: Franklyn Seabra Rogério Bezerra
#curso: Ciências da computação, cadeira de Fundamentos de programação
#professor: José Maria Da Silva Monteiro Filho

#questão 1 lista 8
dados = []
somaSalario = 0.0
somaFilhos = 0.0
percMulher = 0
maiorSalario = 0.0

for i in range(20):
  print("Habitante %d" %(i+1))
  salario = float(input("Digite o salário:"))
  somaSalario += salario
  if salario > maiorSalario:
    maiorSalario = salario
  
  idade = int(input("Digite a idade: "))
  
  sexo = int(input("1 - masculino\n2 - feminino\nDigite o sexo:"))
  if sexo == 2 and salario > 10000:
    percMulher += 1
  
  numFilhos = int(input("Digite a quantidade de filhos:"))
  somaFilhos += numFilhos
  
  habitante = {"salario":salario, "idade":idade, "sexo":sexo, "numFilhos":numFilhos}
  dados.append(habitante)
percMulher = (percMulher*100)/percMulher
  
print("A média dos salarios é R$", somaSalario/20)
print("A média do número de filhos é ", somaFilhos/20)
print("O maior salário registrado foi ", maiorSalario)
print("O percentual de mulheres com salário superior a R$ 10.000,00 é {n}%".format(n=percMulher)) 