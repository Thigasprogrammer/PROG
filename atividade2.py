#Thiago de Aguiar da Silva
#Data: 18/03/2025
#Serra, Brasil
#Esse programa recebe os valores dos coeficientes de uma função de segundo grau e retorna seus coeficientes e suas raizes	

def f_delta(A:float, B:float, C:float)->tuple:
	#declaração de var
	delta = float()

	#processamento
	delta = B**2 - 4*A*C
	return delta

def f_roots(A:float, B:float, C:float)->tuple:
	#declaração de var
	Roots = tuple()
	Root1 = float()
	Root2 = float()
	delta = float()

	#processamento
	delta = f_delta(A, B, C)
	if delta >= 0:
		Root1 = (-B + (delta)**(1/2))/(2*A)
		Root2 = (-B - (delta)**(1/2))/(2*A)
		Roots = (Root1, Root2) #tupla de raizes, para caso não entre no if retornar uma tupla vazia
	return Roots

def main():
	#declaração de var
	A = float()
	B = float()
	C = float()
	Roots = tuple()

	# entrada de dados
	A = float(input())
	B = float(input())
	C = float(input())

	# processamento
	while not(A==0 and B==0 and C==0): #enquanto os coeficientes forem diferentes de 0 o while contiuará
		Roots = f_roots(A, B, C)
		if not(len(Roots)==0): #tupla cheia
			print("a=%.2f b=%.2f c=%.2f r1=%.2f r2=%.2f" % (A, B, C, Roots[0], Roots[1]))
			

		else: #tupla vazia
			print("a=%.2f b=%.2f c=%.2f sem raizes reais" % (A, B, C))
			
		A = float(input())
		B = float(input())
		C = float(input())

if __name__ == '__main__':
	main()
#Thiago de Aguiar da Silva
#Data: 18/03/2025
#Serra, Brasil
#Esse programa recebe os valores dos coeficientes de uma função de segundo grau e retorna seus coeficientes e suas raizes	

def f_delta(A:float, B:float, C:float)->tuple:
	#declaração de var
	delta = float()

	#processamento
	delta = B**2 - 4*A*C
	return delta

def f_roots(A:float, B:float, C:float)->tuple:
	#declaração de var
	Roots = tuple()
	Root1 = float()
	Root2 = float()
	delta = float()

	#processamento
	delta = f_delta(A, B, C)
	if delta >= 0:
		Root1 = (-B + (delta)**(1/2))/(2*A)
		Root2 = (-B - (delta)**(1/2))/(2*A)
		Roots = (Root1, Root2) #tupla de raizes, para caso não entre no if retornar uma tupla vazia
	return Roots

def main():
	#declaração de var
	A = float()
	B = float()
	C = float()
	Roots = tuple()

	# entrada de dados
	A = float(input())
	B = float(input())
	C = float(input())

	# processamento
	while not(A==0 and B==0 and C==0): #enquanto os coeficientes forem diferentes de 0 o while contiuará
		Roots = f_roots(A, B, C)
		if not(len(Roots)==0): #tupla cheia
			print("a=%.2f b=%.2f c=%.2f r1=%.2f r2=%.2f" % (A, B, C, Roots[0], Roots[1]))
			

		else: #tupla vazia
			print("a=%.2f b=%.2f c=%.2f sem raizes reais" % (A, B, C))
			
		A = float(input())
		B = float(input())
		C = float(input())

if __name__ == '__main__':
	main()
