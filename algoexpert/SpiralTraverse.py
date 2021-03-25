def spiralTraverse(array):
	rows = len(array)
	columns = len(array[0])
	count = rows * columns
	result = []
	currentRow = currentCol = 0

	while count > 0:
		startRow = currentRow; startCol = currentCol
		#leftToRight
		while currentCol < columns:
			result.append(array[currentRow][currentCol])
			currentCol += 1
			count -= 1
		currentRow += 1
		currentCol -= 1
		############

		#topToBottom
		while currentRow < rows and count > 0:
			result.append(array[currentRow][currentCol])
			currentRow += 1
			count -= 1
		currentRow -= 1
		currentCol -= 1
		############

		#rightToLeft
		while currentCol >= startCol and count > 0:
			result.append(array[currentRow][currentCol])
			currentCol -= 1
			count -= 1
		currentCol += 1
		currentRow -= 1
		############

		#bottomUp
		while currentRow > startRow and count > 0:
			result.append(array[currentRow][currentCol])
			currentRow -= 1
			count -= 1
		currentRow += 1
		currentCol += 1
		#########
		rows -= 1
		columns -= 1

	return result


if __name__ == "__main__":
	print(spiralTraverse([
		[1,	 2,  3,  4],
		[12, 13, 14, 5],
		[11, 16, 15, 6],
		[10, 9,  8,  7],
	]))
	print(spiralTraverse([[1]]))
	print(spiralTraverse([
		[1, 2, 3, 4],
		[10, 11, 12, 5],
		[9, 8, 7, 6]
	]))
	print(spiralTraverse([
		[1],
		[3],
		[2],
		[5],
		[4],
		[7],
		[6]
	]))
	print(spiralTraverse([[1],[3],[2],[5],[4],[7],[6]]))
