'''
an array is monotonic if it is either monotone increason or monotone decreasing
An array A is monotone increasing if for all i <= j A[i] <= A[j]
An array A is monotone decreasing if for all i <= j A[i] >= A[j]
'''
def isMonotonic(array):
	if array is None or len(array) <= 1:
		return True

	i = 0
	while i < len(array) - 1 and array[i] == array[i + 1]:
		i += 1
	if i == len(array) - 1:
		return False

	if array[i] < array[i + 1]:
		while i < len(array) - 1:
			if array[i] > array[i + 1]:
				return False
			i += 1
		return True
	else:
		while i < len(array) - 1:
			if array[i] < array[i + 1]:
				return False
			i += 1
		return True
	
	return 


if __name__ == "__main__":
	print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
	print(isMonotonic([2,2,2,2,3,4,5,10]))
