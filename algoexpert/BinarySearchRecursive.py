def BinarySearch(array,target,start=None,end=None):
    if start == None:
        start = 0
    if end == None:
        end = len(array) - 1

    if start < end:
        index = int((start + end) / 2)

        if array[index] == target:
            return index
        elif array[index] > target:
            return BinarySearch(array, target, start, index - 1)
        else:
            return BinarySearch(array, target, index + 1, end)
    elif start < len(array) and array[start] == target:
        return start
    elif end >= 0 and array[end] == target:
        return end
    else:
        return -1


if __name__ == "__main__":
    print(BinarySearch([1, 5, 23, 111], 122))
