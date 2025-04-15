
import modatv5
def main():
	lst = [10, 14.5, 33.4, 2, -20, 30, 40, 50, 60, -70]
	lst1 = modatv5.ord_list(lst)
	position = modatv5.sequential_search(lst, 50)
	print(position)
	position = modatv5.sequential_search(lst, 40)
	print(position)
	position = modatv5.binary_search(lst1, 70)
	print(position)
	position = modatv5.binary_search(lst1, 40)
	print(position)

if __name__ == '__main__':
	main()
