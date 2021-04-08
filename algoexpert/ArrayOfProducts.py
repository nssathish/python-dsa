def arrayOfProducts(array):
	totalProduct = 1
	for number in array:
		totalProduct *= number
	
	result = []
	for number in array:
		result.append(totalProduct // number)
	
	return result


if __name__ == "__main__":
	print(arrayOfProducts([5, 1, 2, 4]))
