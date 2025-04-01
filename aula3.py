lista1 = [12, 4, 11, 15, 10, 4, 33, 23]
lista2 = lista1.copy() #copia a lista 1
lista3 = lista1[:] #também copia a lista 1
lista4 = []
print(lista1)
print(lista2)
print(lista3)

lista1.sort() #ordena a própria lista ja criada
lista4 = sorted(lista2) #cria uma lista nova com a lista1 ordenada, se não for especificado será em ordem crescente
print(lista1)
print(lista2)
print(lista3)
print(lista4)
lista4.sort(reverse=True) #ordena a própria lista em ordem decrescente
print(lista4)

lista1b = ["pedro", "henrique", "leonardo"]
lista2b = sorted(lista1b)
lista1b.sort(reverse=True) #coloca em ordem alfabética só que ao contrário
print(lista1b)
print(lista2b)
pessoas = [["Joao", 70.5, 1.7], ["Pedro", 58.9, 1.7], ["Ronaldo", 68.8, 1.8]]
pessoas.sort(key=lambda abacaxi:abacaxi[0]) #ordena o valor a partir da posição "o" da primeira lista, o 'abacaxi' é o nome de uma variavel qualquer, 
# Lambda é uma função que recebe o parametro de ordenação, o x(nome da variavel): x(o que ele pega) 
#exemplo: pessoas.sort(key=lambda abacaxi(nome de uma lista qualquer dentro da lista pessoas):abacaxi[1](pega a posição 1 da lista qualquer abacaxi))
print(pessoas)
pessoas.sort(key=lambda abacaxi:abacaxi[1]/abacaxi[2]**2)
print(pessoas)