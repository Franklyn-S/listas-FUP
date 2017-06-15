'''1.19. Criar um algoritmo que carregue uma matriz 12 x 4 com os valores das vendas de
uma loja, em que cada linha represente um mês do ano, e cada coluna, uma semana do
mês. Para fins de simplificação considere que cada mês possui somente 4 semanas.
Calcule e imprima:
- Total vendido em cada mês do ano;
- Total vendido em cada semana durante todo o ano;
- Total vendido no ano.

autor do programa: Frankly Seabra Rogério Bezerra
1° semestre de Ciências da computação
'''
valor_venda = []
ano = 0
for i in range(12):
    valor_venda.append([])
    for j in range(4):
        valor_venda[i].append(int(input("Digite o valor vendidon na semana %i do mês %i :" %(j+1, i+1) )))

for i in range(12):
    mes = 0
    for j in range(4):
        semana = valor_venda[i][j]
        print("O valor da semana ", j + 1, "do mes ", i + 1, "foi ", semana)
        mes = mes + semana
    ano = ano + mes
    print("O valor do mês ", i + 1, "foi ", mes)
print("O total do ano foi: ", ano)