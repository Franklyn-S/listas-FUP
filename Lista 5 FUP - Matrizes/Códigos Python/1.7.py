matriz=[]
imprimir = []

for i in range(0,4):
	matriz.append([])
	for j in range(0,4):
		matriz[i].append(int(input("Digite o valor da linha %i e da coluna %i: " %(i+1,j+1) )))
		if i+j != 3: # Se não pertencer a inversa ele coloca na lista imprimir
			imprimir.append(matriz[i][j])
#imprime a lista
print("Os elementos que não pertencem a diagonal secundária da matriz são:")
print(imprimir)			




