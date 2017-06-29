def soma(n1,n2):
    if n2 == 0:
        return n1
    elif n2 == 1:
        return n1+1
    else:
        return soma(n1+1,n2-1)
n1 = int(input("Digite o primeiro dígito da soma: "))
n2 = int(input("Digite o segundo dígito da soma: "))
print(soma(n1,n2))
