def InsertionSort(array):
    for i in range(1, len(array)):
        x = array[i]
        j = i - 1
        while j >= 0 and array[j] > x:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x

    return array

def InsertionSortRecursive(array, n = 1):
    if n < len(array):
        x = array[n]
        j = n - 1

        while j >= 0 and array[j] > x:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = x

        InsertionSortRecursive(array, n + 1)

    return array

def InsertionSortRecursionHead(array, n = None):
    if n is None:
        n = len(array) - 1
    
    if n > 0:
        InsertionSortRecursionHead(array, n - 1)
        x = array[n]
        j = n - 1

        while j >= 0 and array[j] > x:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = x

    return array

if __name__ == "__main__":
    print(InsertionSort([8, 5, 2, 6, 9, 3, 5, 4, 8, 7]))
    print(InsertionSortRecursive([8, 5, 2, 6, 9, 3, 5, 4, 8, 7]))
    print(InsertionSortRecursionHead([8, 5, 2, 6, 9, 3, 5, 4, 8, 7]))
