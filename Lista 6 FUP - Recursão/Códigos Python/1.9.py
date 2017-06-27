#Gere a série de Fibonacci até o termo de ordem n.
def fib(n):
	if n == 0:
		return 0
	elif n <= 2:
		return 1
	else:
		return(fib(n-1) + fib(n-2))
n = int(input("Digite o termo desejado da série de Fibonacci para imprimi-lá: "))
for i in range(n):
	print(fib(i))	
