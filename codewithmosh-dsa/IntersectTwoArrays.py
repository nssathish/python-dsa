def Intersect(array1, array2):
	length_of_array1 = len(array1)
	length_of_array2 = len(array2)

	sorted_array1 = sorted(array1) # O(n.log(n))
	sorted_array2 = sorted(array2) # O(n.log(n))

	min_loops = min(length_of_array1, length_of_array2)
	
	intersections = []

	i = j = 0
	while i < min_loops and j < min_loops: #O(n)
		element1 = sorted_array1[i]
		element2 = sorted_array2[j]

		if element1 == element2:
			intersections.append(element1)
			i += 1
			j += 1
		elif element1 > element2:
			j += 1
		else:
			i += 1

	return intersections


if __name__ == '__main__':
	print(Intersect([1, 2, 3, 7], [5, 6, 7, 1]))
	print(Intersect([1, 2, 3, 4], [4, 5, 6, 7, 1]))
