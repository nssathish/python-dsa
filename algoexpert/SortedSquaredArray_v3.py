def sortedSquaredArray(array):
	negative_numbers_index = -1
	positive_numbers_index = len(array)
	result = [None] * positive_numbers_index
	left = 0
	right = len(array) - 1
	iterator = right

	while left < right:
		left_squared = array[left] ** 2
		right_squared = array[right] ** 2
		if left_squared < right_squared:
			result[iterator] = right_squared
			right -= 1
		elif left_squared > right_squared:
			result[iterator] = left_squared
			left += 1
		else:
			result[iterator] = left_squared
			iterator -= 1
			result[iterator] = right_squared
			right -= 1
			left += 1

		print(result)
		iterator -= 1
	else:
		if left == right:
			result[iterator] = array[left] ** 2

	return result


if __name__ == "__main__":
	print(f'{[1,2,3,5,6,8,9]} -> {sortedSquaredArray([1,2,3,5,6,8,9])}')
	print(f'{[-5,-4,3,5,6,8,9]} -> {sortedSquaredArray([-5,-4,3,5,6,8,9])}')
	print(f'{[-5,-4,-3]} -> {sortedSquaredArray([-5,-4,-3])}')
	print(f'{[1]} -> {sortedSquaredArray([1])}')
	print(f'{[-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]} -> {sortedSquaredArray([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20])}')
