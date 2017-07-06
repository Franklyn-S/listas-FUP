#!/usr/bin/python
#-*- coding:utf-8 -*-

#author: Franklyn Seabra Rogério Bezerra
#curso: Ciências da computação, cadeira de Fundamentos de programação
#professor: José Maria Da Silva Monteiro Filho

#questão 1 lista 9

contas = {}
for i in range(3):
	numero_conta = input("Digite o número da conta %d\n>>>" %(i+1))
	contas[numero_conta] = 0
run = 1
while run == 1:
	print("#####MENU#####")
	print("0 - Sair do programa")
	print("1 - Creditar")
	print("2 - Debitar")
	print("3 - Transferir")
	print("4 - Ver saldo\n")

	op = str(input("Digite sua opção:\n>>>"))

	if op == "0":
		print("Programa encerrado.")
		run = 0

	elif op == "1":
		conta = input("Digite o número da conta:\n>>>")
		if conta in contas:
			valor_credito = input("Digite a o valor:\n>>>")
			if valor_credito < 0:
				print("O valor não pode ser negativo!\n")
			else:
				contas[conta] += valor_credito
				print("Valor creditado com sucesso!\n")
		else:
			print("Conta não encontrada!\n")

	elif op == "2":
		conta = input("Digite o número da conta:\n>>>")
		if conta in contas:
			valor_debito = input("Digite a o valor:\n>>>")
			if valor_debito < 0:
				print("O valor não pode ser negativo!\n")
			elif valor_debito > contas[conta]:
				print("Saldo insuficiente!\n")
			else:
				contas[conta] -= valor_debito
				print("Valor debitado com sucesso!\n")
		else:
			print("Conta não encontrada!\n")

	elif op == "3":
		conta_origem = input("Digite o número da conta de origem:\n>>>")
		conta_destino = input("Digite o número da conta de destino:\n>>>")
		if conta_origem in contas or conta_destino in contas:
			valor_transferencia = input("Digite a o valor:\n>>>")
			if valor_transferencia < 0:
				print("O valor não pode ser negativo!\n")
			elif valor_transferencia > contas[conta_origem]:
				print("Saldo insuficiente!\n")
			else:
				contas[conta_origem] -= valor_transferencia
				contas[conta_destino] += valor_transferencia
				print("Valor transferido com sucesso!\n")
		else:
			print("Conta(s) não encontrada(s)!\n")
	elif op == "4":
		conta = input("Digite o número da conta:\n>>>")
		print("O seu saldo é %.2f\n" %(contas[conta]))
	else:
		print("Opção inválida!\n")





