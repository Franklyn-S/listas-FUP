def soma(n1,n2):
    if n2 == 0:
        return n1
    elif n2 == 1:
        return n1+1
    else:
        return soma(n1+1,n2-1)

def multi(n1,n2):
	global n
	if n2 == 0 or n1 == 0:
		return 0
	elif n2 == 1:
		return n1
	elif n1 == 1:
		return n2
	else:
		return multi(soma(n1,n),n2-1)

n = int(input("Digite o valor 1: "))
m = int(input("Digite o valor 2: "))
print(multi(n,m))