def greatestThreeNumbers(array):
    first = second = third = None

    for i in range(len(array)):
        if first is None or array[i] >= first:
            first, second, third = array[i], first, second
        elif second is None or array[i] >= second:
            second, third = array[i], second
        elif third is None or array[i] >= third:
            third = array[i]

    return [third, second, first]
        

        
if __name__ == "__main__":
    print(greatestThreeNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
    print(greatestThreeNumbers([8, 7, 7]))
    print(greatestThreeNumbers([7,7,7,7,7,7,7,7,7,7,7]))
    print(greatestThreeNumbers([11, 43, 55]))
