import random
from random import randint
captcha = str(randint(0,9)) + str(randint(0,9)) + str(chr(randint(65,90))) + str(chr(randint(65,90))) + str(chr(randint(97,122))) + str(chr(randint(97,122)))
captcha = list(captcha)
random.shuffle(captcha)
captcha = "".join(captcha)
print("O CAPTCHA É: %s"  %(captcha))

receba = input("Digite o valor do captcha: ")
receba = receba.lower()
receba = list(receba)
captcha = captcha.lower()
captcha = list(captcha)

aux = 0
for i in range(len(captcha)):
	if captcha[i] == receba[i]:
		aux = aux + 1
if aux == len(captcha):
	print("Correto!")
else:
	print("Incorreto!")