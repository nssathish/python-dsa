def LargestNumberInArray(input_array):
	largest = None
	for number in input_array:
		if largest is None or number > largest:
			largest = number
	
	return largest


if __name__ == '__main__':
	print(LargestNumberInArray([100, 200, 1, 2, 3, 3999, 4, 3]))
