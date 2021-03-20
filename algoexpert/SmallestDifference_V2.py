def SmallestDifference(arrayOne, arrayTwo):
	smallestDifference = None
	arrayOne.sort()
	arrayTwo.sort()
	result = []
	i = j = 0

	while i < len(arrayOne) and j < len(arrayTwo):
		diff = abs(arrayOne[i] - arrayTwo[j])
		if diff == 0:
			return [arrayOne[i], arrayTwo[j]]

		if smallestDifference is None or diff < smallestDifference:
			smallestDifference = diff
			result = [arrayOne[i], arrayTwo[j]]

		if arrayOne[i] < arrayTwo[j]:
			i += 1
		else:
			j += 1
	
	return result


if __name__ == "__main__":
	print(SmallestDifference([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]))
