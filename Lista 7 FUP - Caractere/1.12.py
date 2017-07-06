#1.12.Implemente um programa que leia um ano, no formato dddd, e imprime o ano por extendo
unidade = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezena = ["", ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove" ], "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centena = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

ano = input("Digite o ano: ")
ano = list(ano)
if int(ano[0]) >= 1:
	if int(ano[1]) >=1:
		if int(ano[2]) != 1:
			print(unidade[int(ano[0])] + " mil " + centena[int(ano[1])] + " e " + dezena[int(ano[2])] + " e " + unidade[int(ano[3])])
		else:
			print(unidade[int(ano[0])] + " mil " + centena[int(ano[1])] + " e " + dezena[int(ano[2])][int(ano[3])])
	else:
		if int(ano[2]) != 1:
			print(unidade[int(ano[0])] + " mil "+ "e" +dezena[int(ano[2])] + " e " + unidade[int(ano[3])])
		else:
			print(unidade[int(ano[0])] + " mil " + "e " + dezena[int(ano[2])][int(ano[3])])
else:
	print(centena[int(ano[1])] + dezena[int(ano[2])] + " e " + unidade[int(ano[3])]    )