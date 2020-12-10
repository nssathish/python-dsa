def selectionSort(array):
    for i in range(len(array) - 1):
        minindex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minindex]:
                minindex = j

        if minindex != i:
            array[i], array[minindex] = array[minindex], array[i]
    
    return array


if __name__ == "__main__":
    print(selectionSort([8,5,2,6,9,3,5,4,8,7]))
