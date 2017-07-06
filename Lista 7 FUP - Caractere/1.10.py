# -*- coding: utf-8 -*-
#1.10.	Faça um programa para validar uma senha digitada pelo usuário.
#A senha deve ter pelo menos uma letra maiúscula, pelo menos uma letra minúscula, 
#pelo menos um dígito, deve ter no mínimo 8 e no máximo 15 caracteres.

senha = input("Digite uma senha: ")
maiuscula = False
minuscula = False
digito = False
listaSenha = list(senha)

if len(senha) >= 8 and len(senha) <=15:
	for i in range(len(senha)):
		if listaSenha[i].isupper():
			maiuscula = True
		if listaSenha[i].islower():
			minuscula = True
		if listaSenha[i].isdigit():
			digito = True
	if maiuscula == True and minuscula == True and digito == True:
		print("A senha é válida!")
	else:
		print("A senha deve ter pelo menos uma letra maiúsculae, pelo menos uma letra minúscula e pelo menos um dígito ")

else:
	print("A senha deve ter no mínimo 8 e no máximo 15 caracteres")