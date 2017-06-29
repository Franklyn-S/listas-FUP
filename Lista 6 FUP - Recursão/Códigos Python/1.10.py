#1.10. Calcule o somatório dos n primeiros números inteiros.
def somatorio(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return n + somatorio(n-1)

n = int(input("Digite o valor para somar até ele: "))
print (somatorio(n))