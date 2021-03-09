def sortedSquaredArray(array):
	negative_numbers = []
	negative_numbers_start_index = None

	positive_numbers = []
	positive_numbers_start_index = None

	result = []

	for i in range(len(array)):
		if array[i] < 0:
			negative_numbers.append(array[i] * array[i])
			negative_numbers_start_index = i
		else:
			if positive_numbers_start_index is None:
				positive_numbers_start_index = 0
			positive_numbers.append(array[i] * array[i])

	i = negative_numbers_start_index
	j = positive_numbers_start_index
	negative_number_squared = positive_number_squared = None

	while (i is not None and i >= 0) or (j is not None and j < len(positive_numbers)):
		if i is not None and i >= 0:
			negative_number_squared = negative_numbers[i]
		else:
			negative_number_squared = None

		if j is not None and j < len(positive_numbers):
			positive_number_squared = positive_numbers[j]
		else:
			positive_number_squared = None

		if negative_number_squared is not None and positive_number_squared is not None:
			if negative_number_squared < positive_number_squared:
				result.append(negative_number_squared)
				i -= 1
			elif negative_number_squared > positive_number_squared:
				result.append(positive_number_squared)
				j += 1
			else:
				result.append(negative_number_squared)
				result.append(positive_number_squared)
				i -= 1
				j += 1
		elif negative_number_squared is None and positive_number_squared is not None:
			result.append(positive_number_squared)
			j += 1
		elif negative_number_squared is not None and positive_number_squared is None:
			result.append(negative_number_squared)
			i -= 1

	return result


if __name__ == "__main__":
	array = [-4, -1]
	array = [1, 2, 3, 4]
	array = [-5, -3, 1, 2, 3, 4]
	print(sortedSquaredArray(array))
