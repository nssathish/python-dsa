def fourNumberSum(array, targetSum):
    result = []
    cache = dict()

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            cache[(array[i], array[j])] = sum([array[i], array[j]])

    print(sorted(cache.keys()))

if __name__ == "__main__":
    array = [-1, 22, 18, 4, 7, 11, 2, -5, -3]
    targetSum = 30
    fourNumberSum(array, targetSum)
