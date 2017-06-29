#1.13. Inverta os elementos de um vetor.
def inverter(array, posicao):
	if posicao<len(array)/2:
		tmp = array[posicao]
		nova_posicao = len(array)-posicao-1
		array[posicao] = array[nova_posicao]
		array[nova_posicao] = tmp
		inverter(array, posicao+1)

n = [-1, -2, -6, -5]
inverter(n, 0)
print(n)