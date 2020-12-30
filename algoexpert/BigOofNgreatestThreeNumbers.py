def greatestThreeNumbers(array):
    first = None
    second = None
    third = None

    for i in range(len(array)):
        if first is None or array[i] >= first:
            first = array[i]

    for i in range(len(array)):
        if array[i] != first:
            if (second is None or (array[i] >= second and array[i] < first)):
                second = array[i]

    if second is None:
        second = first

    for i in range(len(array)):
        if array[i] not in [first, second]:
            if (third is None or (array[i] >= third and array[i] < second and array[i] < first)):
                third = array[i]

    if third is None:
        third = second

    return [first, second, third]


if __name__ == "__main__":
    print(greatestThreeNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
    print(greatestThreeNumbers([8, 7, 7]))
