def firstDuplicateValue(array):
	firstDupeIndex = None
	for i in range(len(array)):
		for j in range(i + 1, len(array)):
			if array[i] == array[j] and (firstDupeIndex is None or j < firstDupeIndex):
				firstDupeIndex = j
	
	return array[firstDupeIndex] if firstDupeIndex is not None else -1

if __name__ == "__main__":
	print(firstDuplicateValue([6, 15, 7, 10, 9, 14, 10, 1, 10, 1, 2, 11, 1, 6, 8]))
