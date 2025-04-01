#Thiago de Aguiar da Silva
#Data: 11/03/2025
#Serra, Brasil
#Esse programa calcula a média de salários de um grupo de N pessoas.



def main():
	#declaração de var
	N = int()
	salario = float() 
	media = float()
	#entrada de dados
	N = int(input())
	#processamento
	media = 0; salario = 0
	if N > 0:
		for i in range(N):
			salario = float(input())
			media = media + salario
		media = media/N
		print("MEDIA DOS SALARIOS=%.2f" % media)

	else:
		print("SEM PESSOAS")


if __name__ == "__main__":
	main()