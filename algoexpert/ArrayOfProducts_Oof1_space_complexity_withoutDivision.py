def arrayOfProducts(array):
	result = []

	leftRunningProduct = 1
	for i in range(len(array)):
		result.append(leftRunningProduct)
		leftRunningProduct *= array[i]
	
	rightRunningProduct = 1
	for i in range(len(array) - 1, -1, -1):
		result[i] *= rightRunningProduct
		rightRunningProduct *= array[i]
	
	return result


if __name__ == "__main__":
	print(arrayOfProducts([5, 1, 4, 2]))
