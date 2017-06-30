'''1.3.	Escreva um programa que leia uma cadeia de caracteres (string)
que represente o nome completo de uma pessoa e imprima o mesmo nome 
no formato indicado nos exemplos a seguir. Se a String recebida for
“Maria de Sá Santos” o programa deve imprimir “Santos, Maria de Sá”.
Se a String recebida for “Pedro de Souza” o programa deve imprimir
“Souza, Pedro de”.
'''
nome = input("Digite um nome completo: ")
lista = nome.split()
nome2 = lista[:-1]
if len(nome2) == 2:
	nome2.insert(1, " ")
sobrenome = lista[-1]
novoNome =  ''.join([sobrenome] + [', '] + nome2)
print(novoNome)