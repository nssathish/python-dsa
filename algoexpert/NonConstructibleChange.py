def nonConstructibleChange(coins):
	'''
		13, 15, 22, 23
		1 1 2 3 5 7 22

		coin    constructiblechange
		1       1 -> 2
		1       2 -> 3
		2       3 -> 5
		3       5 -> 8
		5       8 -> 13
		7       13 -> 20
		22      return 20
	'''
	constructibleChange = 1
	coins.sort()
	for coin in coins:
		if coin > constructibleChange:
			return constructibleChange
		constructibleChange += coin
	
	return constructibleChange

if __name__ == "__main__":
	print(nonConstructibleChange([1, 2, 5]))
	print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22])

