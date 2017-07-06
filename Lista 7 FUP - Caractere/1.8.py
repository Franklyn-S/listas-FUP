#1.8.Implemente um programa que leia uma cadeia de caracteres e um número inteiro positivo “n”.
#O programa deve imprimir todas as sub-cadeias da cadeia original de comprimento igual a “n”.
cadeia = input("Digite uma cadeia de caracteres: ")
num = int(input("Digite um número inteiro e positivo: "))
for i in range(len(cadeia)):
	print(cadeia[i:num])