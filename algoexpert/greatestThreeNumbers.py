def mergeSort(array):
    for i in range(len(array) - 1):
        j = i + 1
        while (array[i] > array[j]):
            j += 1


if __name__ == "__main__":
    result = insertionSort([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
    return [result[len(result) - 3], result[len(result) - 2], result[len(result) - 1]]
