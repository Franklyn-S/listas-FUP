tombos = []
obras = []
for i in range(20):
  numeroTombo = i
  nomeObra = "teste%d" % (i+1)
  nomeAutor = "autor%d" % (i+1)
  nomeEditora = "editora%d" % (i+1)
  ano = int("200"+str(i))
  tombo = {"numeroTombo":numeroTombo, "nomeObra":nomeObra, "nomeAutor":nomeAutor, "nomeEditora": nomeEditora, "ano":ano}
  
  tombos.append(tombo)
  obras.append([])
  for j in range(3):
    numExemplar = j+1
    dataCompra = "11/07/2017"
    obra = {"numeroTombo":numeroTombo, "numExemplar":numExemplar, "dataCompra":dataCompra}
    obras[i].append(obra)

'''   
print(tombos)
print("\n")
print(obras)
'''    

def CadastrarTombo():
  novoNumeroTombo = int(input("Digite o número do Tombo:"))
  novoNomeObra = input("Digite o nome da obra:")
  novoNomeAutor = input("Digite o nome do autor:")
  novoNomeEditora = input("Digite o nome da editora:")
  novoAno = int(input("Digite o ano do Tombo:"))
  
  novoTombo = {"numeroTombo":novoNumeroTombo, "nomeObra":novoNomeObra, "nomeAutor":novoNomeAutor, "nomeEditora": novoNomeEditora, "ano":novoAno}
  tombos.append(novoTombo)
  print("\nTombo cadastrado com sucesso!")
  
def CadastrarObra():
  novoNumeroTombo = int(input("Digite o número do tombo:"))
  novoNumExemplar = int(input("Digite o número do exemplar:"))
  novaDataCompra = input("Digite  data ultima da compra")
  novaObra = {"numeroTombo":novoNumeroTombo, "numExemplar":novoNumExemplar, "dataCompra":novaDataCompra}
  obras[novoNumeroTombo].append(novaObra)
  print("\nObra cadastrada com sucesso!")
  
def mostrarPorAno():
  novoAno = input("Digite o ano:")
  for dic in tombos:
    if dic["ano"] == novoAno:
      print(dic)
      return l
def mostrarPorAutor():
  novoNomeAutor = input("Digite o nome do autor:")
  for dic in tombos:
    if dic["nomeAutor"] == novoNomeAutor:
      print(dic)
      return l
def mostrarPorEditora():
  novoNomeEditora = input("Digite o nome da editora:")
  for dic in tombos:
    if dic["nomeAutor"] == novoNomeAutor:
      print(dic)
      return l

entrada = 0
while entrada != 6:
  print("###MENU###")
  print("1. Cadastrar tombo;")
  print("2. Cadastrar obra;")
  print("3. Mostrar obras por ano, onde o ano é fornecido pelo usuário;")
  print("4. Mostrar obras por autor, onde o nome do autor é fornecido pelo usuário;")
  print("5. Mostrar obras por editora;")
  print("6. Encerrar o programa.\n")
  entrada = int(input("Digite sua opção:"))
  if entrada == 1:
    CadastrarTombo()
  elif entrada == 2:
    CadastrarObra()
  elif entrada == 3:
    mostrarPorAno()
  elif entrada == 4:
    mostrarPorAutor()
  elif entrada == 5:
    mostrarPorEditora()
  elif entrada == 6:
    print("Programa encerrado!")