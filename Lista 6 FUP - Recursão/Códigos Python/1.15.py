def inverter(array, posicao):
	if posicao<len(array)/2:
		tmp = array[posicao]
		nova_posicao = len(array)-posicao-1
		array[posicao] = array[nova_posicao]
		array[nova_posicao] = tmp
		inverter(array, posicao+1)

palavra = str(input("Digite uma palavra para verifcar se ela é palíndromo: "))
lista = list(palavra)
palavra_original = lista
inverter(lista, 0)

teste = 0
for i in range(len(palavra_original)):
	if palavra_original[i] == lista[len(palavra_original)-i-1]:
		teste = teste  + 1
if teste == len(palavra_original):
	print("A palavra é um palíndromo")
else:
	print("A palavra NÃO é um palíndromo")

