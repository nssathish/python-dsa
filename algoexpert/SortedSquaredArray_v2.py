def sortedSquaredArray(array):
	result = []
	negative_numbers_start_index = -1
	positive_numbers_start_index = 0

	for i in range(len(array)):
		if array[i] < 0:
			negative_numbers_start_index = i
		else:
			positive_numbers_start_index = i
			break
			
	while negative_numbers_start_index >= 0 or positive_numbers_start_index < len(array):
		if negative_numbers_start_index >= 0 and positive_numbers_start_index < len(array):
			negative_number_squared = array[negative_numbers_start_index] * array[negative_numbers_start_index]
			positive_number_squared = array[positive_numbers_start_index] * array[positive_numbers_start_index]

			if negative_number_squared < positive_number_squared:
				result.append(negative_number_squared)
				negative_numbers_start_index -= 1
			elif negative_number_squared > positive_number_squared:
				result.append(positive_number_squared)
				positive_numbers_start_index += 1
			else:
				result.append(negative_number_squared)
				negative_numbers_start_index -= 1
				result.append(positive_number_squared)
				positive_numbers_start_index += 1
		elif negative_numbers_start_index < 0 and positive_numbers_start_index < len(array):
			positive_number_squared = array[positive_numbers_start_index] * array[positive_numbers_start_index]
			result.append(positive_number_squared)
			positive_numbers_start_index += 1
		elif negative_numbers_start_index >= 0 and positive_numbers_start_index >= len(array):
			negative_number_squared = array[negative_numbers_start_index] * array[negative_numbers_start_index]
			result.append(negative_number_squared)
			negative_numbers_start_index -= 1

				
	return result


if __name__ == "__main__":
	array = [-4, -1]
	array = [-5, -3, 1, 2, 3, 4]
	array = [1, 2, 3, 4]
	print(sortedSquaredArray(array))
