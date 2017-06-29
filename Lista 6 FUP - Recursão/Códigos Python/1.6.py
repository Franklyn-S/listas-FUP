n = int(input('Escreva um numero natural n: '))

def permutacoes(lista, passo = 0):
    if passo == len(lista):
        print ("".join(lista))
        
    for i in range(passo, len(lista)):
        copia_lista = list(lista)
        copia_lista[passo], copia_lista[i] = copia_lista[i], copia_lista[passo]
        permutacoes(copia_lista, passo + 1)

def gerarComb(n):
    letras = [chr(i) for i in range(65, 65 + n)]
    permutacoes(letras)
    
gerarComb(n)
