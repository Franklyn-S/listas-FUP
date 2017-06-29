#1.11. Calcule a soma de todos os valores de um array de reais.
def somatorio(v):
	if v>1:
		return n[v-1] + somatorio(v-1)
	else:
		return n[0]


n = [1.1, 1.2, 1.3]
print (somatorio(len(n)))