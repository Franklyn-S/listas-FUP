#1.5.Implemente um programa que leia uma cadeia de caracteres e um caractere.
#O programa deve retirar da cadeia todas as ocorrências desse caractere.
#Imprimir a nova cadeia.
cadeia = input("Digite uma frase: ")
caractere = input("Digite um caractere para remover da frase: ")
#calcula a quantidade de caracteres
quantidade = cadeia.count(caractere)
listaCadeia = list(cadeia)
for i in range(quantidade):
	listaCadeia.remove(caractere)
nova_cadeia = "".join(listaCadeia)
print("frase sem o", caractere)
print(nova_cadeia)