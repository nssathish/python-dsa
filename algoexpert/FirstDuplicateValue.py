def firstDuplicateValue(array):
	store = {}
	firstDupePosition = None

	for i in range(len(array)):
		item = array[i]
		if item not in store:
			store[item] = None
		else:
			store[item] = i
	
	for i in range(len(array)):
		item = array[i]
		if store[item] is not None:
			if firstDupePosition is None or store[item] < firstDupePosition:
				firstDupePosition = store[item]
	
	return array[firstDupePosition] if firstDupePosition is not None else -1


if __name__ == "__main__":
	print(firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]))
	print(firstDuplicateValue([2, 1, 5, 3, 3, 2, 4]))
