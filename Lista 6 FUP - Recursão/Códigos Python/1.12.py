#1.12. Encontre o maior elemento de um array de inteiros.
def maiorElem(t, maior):
	if t == 0:
		return 0
	elif t == 1:
		return maior
	else:
		if n[t-1] > maior:
			return(maiorElem(t-1, n[t-1]))
		else:
			return(maiorElem(t-1, maior))

n = [-1, -2, -6, -5]
print(maiorElem(len(n), n[0]))