def mergeContinuousIntervals(intervals):
	intervals.sort() #O(nlog(n)) time
	result = list() #O(n) space
	i = 0
	while i < len(intervals):
		currentInterval = intervals[i]

		while i < len(intervals) - 1:
			nextInterval = intervals[i + 1]

			if currentInterval[1] >= nextInterval[0]:
				currentInterval = [min(currentInterval[0], nextInterval[0]), max(currentInterval[1], nextInterval[1])]
				i += 1
			else:
				break

		result.append(currentInterval)
		i += 1

	return result


if __name__ == "__main__":
	print(mergeContinuousIntervals([[1,2], [3, 5], [4, 7], [6, 8], [9, 10]]))
	print(mergeContinuousIntervals([[100,105], [1, 104]]))
	print(mergeContinuousIntervals([[89, 90], [-10, 20], [-50, 0], [70, 90], [90, 91], [90, 95]]))
	print(mergeContinuousIntervals([[20, 21], [22, 23], [0, 1], [3, 4], [23, 24], [25, 27], [5, 6], [7, 19]]))
	print(mergeContinuousIntervals([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
