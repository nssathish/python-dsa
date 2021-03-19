def SmallestDifference(firstArray, secondArray):
	#firstArray.sort()
	#secondArray.sort()
	smallestDifference = None
	resultSet = {}

	for first in firstArray:
		for second in secondArray:
			diff = abs(first - second)
			if smallestDifference is None or diff < smallestDifference:
				smallestDifference = diff
				resultSet = set([first, second])
	
	return resultSet


if __name__ == "__main__":
	'''
	[-5, 1, 10, 20, 28, 3], 
	-5, 1, 3, 10, 20, 28
	15, 17, 26, 134, 135
	[26, 134, 135, 15, 17]
	'''
	print(SmallestDifference([-5, 1, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
	print(SmallestDifference([26, 134, 135, 15, 17], [-5, 1, 10, 20, 28, 3]))
