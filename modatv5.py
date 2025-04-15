'''esta função recebe como parametro de entrada uma lista de num reais
retorna a posição de primeira ocorrencia, se não tiver retorna -1
ou seja vai retornar em qual posição aparece pela primeira vez
def sequential_search(data: list, element: float) -> int:
	size = len(data)
	if not(element in data):
			return -1

	else:
		for i in range(size):
			if data[i] == element:
				return i
'''

def sequential_search(data: list, element: float) -> int:
	#declarando variaveis
	i = int()
	position = int()
	#processamento
	position = -1
	i = 0
	while  i < len(data):
		if element == data[i]:
			position = i
		i = i + 1

	return position

def binary_search(data: list, element: float) -> int:
	data = ord_list(data)
	#declarando variaveis
	start = int()
	middle = int()
	end = int()
	i = int()
	position = int()

	#processamento
	start = 0
	end = len(data) - 1
	position = -1

	while start <= end and position == -1:
		middle = (end + start) // 2

		if element == data[middle]:
			position = middle

		else:
			if element > data[middle]:
				start = middle + 1

			else:
				end = middle - 1


	return position

def ord_list(lst:list):
	lst_ord = sorted(lst)


	return lst_ord



