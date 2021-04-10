def arrayOfProducts(array):
	result = []
	leftProducts = [1 for _ in range(len(array))]
	rightProducts = [1 for _ in range(len(array))]
	
	leftRunningProduct = 1
	for i in range(len(array)):
		leftProducts[i] = leftRunningProduct
		leftRunningProduct *= array[i]
	
	rightRunningProduct = 1
	print(rightProducts)
	for i in range(len(array) - 1, -1, -1):
		print([i, array[i]])
		rightProducts[i] *= rightRunningProduct
		rightRunningProduct *= array[i]
	
	for i in range(len(array)):
		result.append(leftProducts[i] * rightProducts[i])
	
	return result

if __name__ == "__main__":
	print(arrayOfProducts([5, 1, 2, 4]))
