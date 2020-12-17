def BinarySearch(array, element):
	start = 0; end = len(array); n = 1

	while start < end:
		print(f'n={n} start={start} end={end}')

		if element < array[n]:
			end = n - 1
		else:
			start = n + 1
		
		n = int((start + end) / 2)
	else:
		if start < len(array) and array[start] == element:
			return start
		if end > 0 and end < len(array) and arra[end] == element:
			return end
		return -1


if __name__ == "__main__":
	array = list(map(int,"1 2 3 4 5 6 7 8 9".split(' ')))
	array = list(map(int,"0 1 21 33 45 45 61 71 72 73".split(' ')))
	array = list(map(int,"1 5 23 111".split(' ')))
	element = 3
	print(BinarySearch(array, 122))
