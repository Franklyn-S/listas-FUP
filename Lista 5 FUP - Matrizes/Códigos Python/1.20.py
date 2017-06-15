'''1.20. Uma matriz M contém na 1ª coluna a matrícula do aluno no curso; na 2ª coluna, o
sexo (0 para feminino e 1 para masculino); na 3ª, o código do curso, e na 4ª, o CR
(Coeficiente de Rendimento). Suponha que o CR é um número inteiro. Faça um
programa que leia os dados de 10 alunos e armazene esses dados na matriz M. Um
grupo empresarial resolveu premiar a aluna com CR mais alto de um curso cujo código
deverá ser digitado. O programa deve receber o código do curso e imprimir a matrícula
da aluna que deve ser premiada. Caso existam mais de uma aluna com o CR mais alto,
imprimir a matrícula de todas elas.

autor do programa: Franklyn Seabra Rogério Bezerra
1° semestre Ciências da Computação - UFC
'''

m = []
for i in range(2):
    m.append([])
    print("***NOVO ALUNO***")
    for j in range(4):
        if j == 0:
            m[i].append(int(input("Digite a matricula: ")))
        elif j == 1:
            m[i].append(int(input("Digite o sexo(0 para feminino e 1 para masculino: ")))
        elif j == 2:
            m[i].append(int(input("Digite o código do curso: ")))
        elif j == 3:
            m[i].append(int(input("Digite o Coeficiente de Rendimento(CR): ")))

digito_curso = int(input("Digite o dígito do curso para escolher o aluno premiado: "))

maior = 0
#acha a maior nota do curso digitado
for i in range(2):
    if m[i][3] > maior and m[i][2] == digito_curso:
        maior = m[i][3]
#imprime os alunos com a maior nota no curso digitado
for i in range(2):
    if m[i][3] == maior and m[i][2] == digito_curso:
        print("O aluno de matricula", m[i][0], "foi premiado")
if maior == 0:
    print("Dígite de curso inválido")









