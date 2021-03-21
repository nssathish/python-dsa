def moveElementToEnd(array, toMove):
	i = 0
	j = len(array) - 1

	while i < j:
		if array[i] == toMove:
			if array[i] != array[j]:
				array[i], array[j] = array[j], array[i]
				i += 1
			j -= 1
		elif array[i] != toMove:
			i += 1

	return array


if __name__ == "__main__":
	print(moveElementToEnd([2,1,2,2,2,3,4,2], 2))
