#1.6.Implemente um programa que leia uma cadeia de caracteres e imprima todos os prefixos dessa cadeia.
cadeia = input("Digite uma cadeia de caracteres: ")
print("Seus prefixos: ")
for i in range(len(cadeia)):
	print(cadeia[0:i])