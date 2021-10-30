def Reverse(array):
	return [array[i] for i in range(len(array) - 1, -1, -1)]


if __name__ == '__main__':
	print(Reverse([2, 3, 1, 24, 5]))
	print(Reverse([23, 521, 21, 1]))
