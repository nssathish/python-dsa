def isMonotonic(array):
	if len(array) <= 2:
		return True

	direction = array[0] - array[1]
	for i in range(1, len(array) - 1):
		#print(f'direction: {direction}')
		if direction == 0:
			direction = array[i] - array[i + 1]
			continue
		if breaksDirection(direction, array[i], array[i + 1]):
			return False
	return True

def breaksDirection(direction, currentItem, nextItem):
	diff = currentItem - nextItem
	if direction < 0:
		return diff > 0
	
	return diff < 0


if __name__ == "__main__":
	print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -9001]))
	print(isMonotonic([1, 2, 0]))
	print(isMonotonic([-1, -5, 10]))
