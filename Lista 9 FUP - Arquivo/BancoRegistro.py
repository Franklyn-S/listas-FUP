#!/usr/bin/python
#-*- coding:utf-8 -*-

#author: Franklyn Seabra Rogério Bezerra
#curso: Ciências da computação, cadeira de Fundamentos de programação
#professor: José Maria Da Silva Monteiro Filho

#questão 1 lista 9

contas = []
#contas = [{numero_conta:saldo} {numero_conta2:saldo2}]
run = 1
while run == 1:
	print ("#####MENU#####")
	print ("0 - Sair do programa")
	print ("1 - Creditar")
	print ("2 - Debitar")
	print ("3 - Transferir")
	print ("4 - Ver saldo")
	print ("5 - Criar conta")
	print ("6 - Excluir conta\n")

	op = input("Digite sua opção:\n>>>")

	if op == "0":
		print ("Programa encerrado.")
		run = 0

	elif op == "1":
		conta = input("Digite o número da conta:\n>>>")
		if len(contas) == 0:
			print("Nenhuma conta foi criada")
		else:
			existe = False
			i = 0
			while  i < len(contas) and existe == False:
				if conta in contas[i]:
					existe = True
				i = i+1
			if existe:
				valor_credito = int(input("Digite o valor a ser creditado:\n>>>"))
				if valor_credito <= 0:
					print ("valor inválido!\n")
				else:
					contas[i-1][conta] += valor_credito
					print ("Valor creditado com sucesso!\n")
			else:
				print ("Conta não encontrada!\n")


	elif op == "2":
		conta = input("Digite o número da conta:\n>>>")
		if len(contas) == 0:
			print("Nenhuma conta foi criada")
		else:
			existe = False
			i = 0
			while  i < len(contas) and existe == False:
				if conta in contas[i]:
					existe = True
				i = i+1
			if existe:
				valor_debito = int(input("Digite o valor a ser debitado:\n>>>"))
				if valor_debito <= 0:
					print ("valor inválido!\n")
				elif valor_debito > contas[i-1][conta]:
					print ("Saldo insuficiente!\n")
				else:
					contas[i-1][conta] -= valor_credito
					print ("Valor debitado com sucesso!\n")
			else:
				print ("Conta não encontrada!\n")

	elif op == "3":
		conta_origem = input("Digite o número da conta origem:\n>>>")
		conta_destino = input("Digite o número da conta destino:\n>>>")
		if len(contas) == 0:
			print("Nenhuma conta foi criada")
		else:
			existe_origem = False
			i = 0
			while  i < len(contas) and existe_origem == False:
				if conta_origem in contas[i]:
					existe_origem = True
				i = i+1

			existe_destino = False
			j = 0
			while  j < len(contas) and existe_destino == False:
				if conta_destino in contas[j]:
					existe_destino = True
				j = j+1

			if existe_origem and existe_destino:
				valor_transferencia = int(input("Digite o valor a ser transferido:\n>>>"))
				if valor_transferencia <= 0:
					print ("valor inválido!\n")
				elif valor_transferencia > contas[i-1][conta_origem]:
					print ("Saldo insuficiente!\n")
				else:
					contas[i-1][conta_origem] -= valor_transferencia
					contas[j-1][conta_destino] += valor_transferencia
					print ("Valor transferido com sucesso!\n")
			else:
				print ("Conta não encontrada!\n")

			
	elif op == "4":
		conta = input("Digite o número da conta:\n>>>")
		if len(contas) == 0:
			print("Nenhuma conta foi criada")
		else:
			existe = False
			i = 0
			while  i < len(contas) and existe == False:
				if conta in contas[i]:
					existe = True
				i = i+1
			if existe:
				print("Seu saldo é %.2f\n" %(contas[i-1][conta]))
			else:
				print ("Conta não encontrada!\n")
	
	elif op == "5":
		numero_conta = input("Digite o número da conta \n>>>" )
		if len(contas) == 0:
			dic = {numero_conta:0}
			contas.append(dic)
			print("Conta criada com sucesso!\n")
		else:
			existe = False
			i = 0
			while  i < len(contas) and existe == False:
				if numero_conta in contas[i]:
					existe = True
				i = i+1
			if existe:
				print("A conta já existe\n")
			else:
				dic = {numero_conta:0}
				contas.append(dic)
				print("\nConta criada com sucesso!\n")
				print(contas)
		
	elif op == "6":
		numero_conta = input("Digite o número da conta\n>>>" )
		if len(contas) == 0:
			print("Nenhuma conta foi criada")
		else:
			existe = False
			i = 0
			while  i < len(contas) and existe == False:
				if numero_conta in contas[i]:
					existe = True
				i = i+1
			if existe:
				contas.pop(i-1)
				print("\nA conta foi removida\n")
			else:
				print("A conta não existe\n")

	else:
		print ("Opção inválida!\n")