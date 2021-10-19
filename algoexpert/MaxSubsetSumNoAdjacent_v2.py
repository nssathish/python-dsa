def maxSubSetSumNoAdjacent(array):
	if len(array) == 0:
		return 0
	
	if len(array) == 1:
		return array[0]
	
	array[1] = max(array[0], array[1])
	for i in range(2, len(array)):
		array[i] = max(array[i - 1], array[i - 2] + array[i])
	
	return array.pop()


if __name__ == '__main__':
	print(maxSubSetSumNoAdjacent([7, 10, 12, 7, 9, 14]))
