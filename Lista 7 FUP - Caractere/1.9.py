# -*- coding: utf-8 -*-
#1.9.Faça um programa para validar um endereço de e-mail digitado pelo usuário.
#O programa deve indicar se o email fornecido é válido ou não.
email = input("Digite seu e-mail: ")
if email.count("@") == 1:
	if email.count(".com") == 1:
		print("É um e-mail válido!")
	else:
		print('Um e-mail precisa de um único ".com" ')
else:
	print('Um e-mail precisa de um único "@" ')