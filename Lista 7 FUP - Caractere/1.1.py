'''
1.1. Escreva um programa que leia uma cadeia de caracteres
(string) e gera uma nova cadeia de caracteres onde todas as
letras minúsculas da cadeia original foram trocadas por 
maiúsculas e vice-versa. Caracteres que não são letras 
(como dígitos, '.', espaço, etc.) não devem ser trocados.
'''
#Método 1 usando a função swapcase
'''
cc = input("Digite uma frase: ")

print("A frase com maiusculas e minusculas trocadas é: ")
cc = cc.swapcase()
print(cc)
'''

#Método 2
alfaMai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P' , 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfaMin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
texto = str(input("Digite uma frase: "))


for i in range(len(texto)):
	for j in range(len(alfaMai)):
		if texto[i] == alfaMai[j]:
			texto[i] = alfaMin[j]
		elif texto[i] == alfaMin[j]:
			texto[i] = alfaMai[j]
print(texto)
