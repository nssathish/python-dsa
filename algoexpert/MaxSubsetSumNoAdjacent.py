def maxSubSetSumNoAdjacent(numbers):
	if len(numbers) == 0: return 0
	if len(numbers) == 1: return numbers[0]
	if len(numbers) == 2: return max(numbers[0], numbers[1])

	maxSums = [numbers[0]]
	maxSums.append(max(numbers[0], numbers[1]))

	for i in range(2, len(numbers)):
		maxSums.append(max(maxSums[i - 1], maxSums[i - 2] + numbers[i]))
	
	return maxSums.pop()


if __name__ == '__main__':
	print(maxSubSetSumNoAdjacent([75, 105, 120, 75, 90, 135]))
