def soma(n1,n2):
    if n2 == 0:
        return n1
    elif n2 == 1:
        return n1+1
    elif n1 == 1:
    	return n2+1
    else:
        return soma(abs(n1)+1,abs(n2)-1)

def multi(n1,n2):
	global n
	if n2 == 0 or n1 == 0:
		return 0
	elif n2 == 1:
		return n1
	elif n1 == 1:
		return n2
	else:
		if n1 > 0 and n2 > 0:
			return multi(soma(n1,n),abs(n2)-1)
		elif n1 < 0 and n2 > 0:
			return -1 * multi(soma(n1,n),abs(n2)-1)
		elif n1 > 0 and n2 < 0:
			return -1 * multi(soma(n1,n),abs(n2)-1)
		elif n1 < 0 and n2 < 0:
			return multi(soma(n1,n),abs(n2)-1)
n = int(input("Digite o valor 1: "))
m = int(input("Digite o valor 2: "))
print(multi(n,m))