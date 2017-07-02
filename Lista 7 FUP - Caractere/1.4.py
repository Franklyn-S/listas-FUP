#1.4.Escreva um programa que leia duas cadeias de caracteres (string) 
#e verifica se uma é anagrama de outra. 
#Anagrama é uma palavra formada pela transposição das 
#letras de outra, como, por exemplo: 'capa' e 'paca'; 'roma' e 'mora'.
string1 = input("Digite a primeira palavra: ")
string2 = input("Digite a segunda palavra: ")
string1 = list(string1)
string2 = list(string2)
if len(string1) == len(string2):
	verificador = 0
	for i in range(0,len(string1)):
		j = 0
		while j < len(string2):
			if string1[i] == string2[j]:
				verificador = verificador + 1
			if string2[i] == string1[j]:
				verificador = verificador + 1
			j = j + 1
	if verificador == 2 * 	len(string1):
		print("São anagramas!")
	else:
		print("Não são anagramas!")	
else:
	print("Não são anagramas!")