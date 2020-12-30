def productSum(array):
    depth = 1
    result = 0
    for item in array:
        if type(item) is int:
            result = result + (depth * item)
        elif type(item) is list:
            depth += 1
            for element in item:
                result = result + (depth * element)

    return result


if __name__ == "__main__":
    print(productSum([1,2,3,4]))
    print(productSum([[[[1,[2,3]]]]]))
