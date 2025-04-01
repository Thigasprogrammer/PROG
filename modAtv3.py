def f_preencherlista(n:int) -> list: #função 1
	nome = str()
	peso = float()
	altura = float()
	lst_pessoas = list()
	lst_dados = list()
	for i in range(n):
 		nome = str(input())
 		peso = float(input())
 		altura = float(input())
 		lst_dados = [nome, peso, altura]
 		lst_pessoas.append(lst_dados)

	return lst_pessoas

def f_calcularIMC(peso: float, altura:float) ->float: #função 2
	IMC = float
	IMC = peso/altura**2

	return IMC

def f_ordIMC(lst_pessoas: list)->list: #função 3
	lst_pessoas.sort(key=lambda lista:f_calcularIMC(lista[1], lista[2]))

	return lst_pessoas


def imprimir(lst_pessoas:list) -> None: #função 4
	tamanho = len(lst_pessoas)
	lst_ordenada = f_ordIMC(lst_pessoas)

	for i in range(tamanho):
		print(lst_ordenada[i][0], "%.2f" % (f_calcularIMC(lst_ordenada[i][1], lst_ordenada[i][2])))
	
