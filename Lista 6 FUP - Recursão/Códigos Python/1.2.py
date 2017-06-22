#Multiplicação de dois números naturais, através de somas sucessivas 
#(Ex.: 6 ∗ 4 = 4 + 4 + 4 + 4 + 4 + 4).
def multi(n1,n2):
	global num1
	if n2 == 0 or n1 == 0:
		return 0
	elif n2 == 1:
		return n1
	else:
		n1 = n1+num1
		return multi(n1, n2-1)
num1 = int(input("Digite um número:"))
num2 = int(input("Digite um segundo número:"))
print(multi(num1,num2))
