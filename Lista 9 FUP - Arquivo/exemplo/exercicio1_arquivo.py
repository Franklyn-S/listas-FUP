arq = open('notas2.txt', 'r')

#printa as linhas do arquivo
'''
for linha in arq:
	print(linha)
'''
Reprovados = {}
Aprovados = {}

#Verifica se o aluno passou ou não
for linha in arq:
	dados = linha.split("	")
	nome = dados[0]
	nota = float(dados[1])
	if nota >= 7:
		Aprovados[nome] = nota
	else:
		Reprovados[nome] = nota
arq.close()
#Grava no arquivo e printa em ordem alfabetica
arq_ap = open("aprovados.txt", 'w')
print("Escreveu no arquivo aprovados.txt")
print("Aprovados:")
for k in sorted(Aprovados):
	print(k, "	", Aprovados[k])
	arq_ap.write(k + "	" + str(Aprovados[k]) + "\n")
arq_ap.close()

arq_rep = open("reprovados.txt", 'w')
print("Escreveu no arquivo reprovados.txt")
print("Reprovados:")
for k in sorted(Reprovados):
	print(k, "	",Reprovados[k])
	arq_rep.write(k + "	" + str(Reprovados[k]) + "\n")
arq_rep.close()