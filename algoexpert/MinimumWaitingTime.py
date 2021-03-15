def minimumWaitingTime(queries):
	queries.sort()
	waitTime = 0
	minWaitTime = 0

	for i in range(len(queries) - 1):
		waitTime += queries[i]
		minWaitTime += waitTime

	return minWaitTime


if __name__ == "__main__":
	print(minimumWaitingTime([3, 2, 1, 2, 6]))
