data = input("Digite a data: ")
data = data.split("/")
if len(data[0]) == 2:
	if int(data[1]) == 2:
		if int(data[0]) <= 29:
			print("A data é válida e o formato é brasileiro!")
		else:
			print("O mês %d só tem 29 dias" %(data[1]))
	elif int(data[1]) <= 12 and int(data[1]) % 2 == 0:
		if int(data[0]) <= 30:
			print("A data é válida e o formato é brasileiro!")
		else:
			print("O mês %d só tem 30 dias" %(data[1]))
	elif int(data[1]) <= 12 and int(data[1]) % 2 != 0:
		if int(data[0]) <= 31:
			print("A data é válida e o formato é brasileiro!")
		else:
			print("O mês %d só tem 31 dias" %(data[1]))
	else:
		print("Data inválida!")
elif len(data[0]) == 4:
	if int(data[1]) == 2:
		if int(data[2]) <= 29:
			print("A data é válida e o formato é americano!")
		else:
			print("O mês %d só tem 29 dias" %(data[1]))
	elif int(data[1]) <= 12 and int(data[1]) % 2 == 0:
		if int(data[2]) <= 30:
			print("A data é válida e o formato é americano!")
		else:
			print("O mês %d só tem 30 dias" %(data[1]))
	elif int(data[1]) <= 12 and int(data[1]) % 2 != 0:
		if int(data[2]) <= 31:
			print("A data é válida e o formato é americano!")
		else:
			print("O mês %d só tem 31 dias" %(data[1]))
	else:
		print("Data inválida!")
else:
	print("Data inválida!")
