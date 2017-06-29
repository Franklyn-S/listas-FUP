#Impressão de um número natural em base binária.
def calc_bin(n):
	if n < 0:
		return "Número negativo"
	elif (n<2):
		return str(n%2)
	else:
		return calc_bin(n//2) + str(n%2)

#Usando lambda é possível fazer em uma linha

#calc_bin = lambda n: str(n%2) if n<2 else calc_bin(n//2) + str(n%2)

n = int(input("Digite um número: "))
print(calc_bin(n))