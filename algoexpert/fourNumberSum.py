def fourNumberSum(array, targetSum):
    array.sort()
    result = []

    for i in range(len(array) - 2):
        left1 = i
        left2 = i + 1
        right1 = len(array) - 2
        right2 = len(array) - 1

        while (left2 < right1):
            elements = [array[left1], array[left2], array[right1], array[right2]]
            print(f'left2 < right1: elements: {elements}')
            if sum(elements) == targetSum:
                print(f'sum(elements) == targetSum: elements: {elements}')
                result.append(elements)
                left2 += 1
                right1 = len(array) - 2
                right2 = len(array) - 1
            elif sum(elements) < targetSum:
                print(f'sum(elements) < targetSum: elements: {elements}')
                left2 += 1
            else:
                right1 -= 1
                while left2 < right1:
                    elements = [array[left1], array[left2], array[right1], array[right2]]
                    print(f'sum(elements) > targetSum: elements: {elements}')
   
                    if sum(elements) == targetSum:
                        print(f'inner if sum(elements) == targetSum: elements: {elements}')
                        result.append(elements)
                    right1 -= 1
                else:
                    right2 -= 1
                    right1 = right2 -1

    return result


if __name__ == "__main__":
    #array = [7,6,4,-1,1,2]
    #targetSum = 16
    array = [-2, 2, -5, 5, -3, 3]
    targetSum = 0
    array = [1, 2, 3, 4, 5, 6, 7]
    targetSum = 10
    array = [-1, 22, 18, 4, 7, 11, 2, -5, -3]
    targetSum = 30
    
    """
    -1 2 7 22
    -3 4 7 22
    -1 2 11 18
    -3 4 11 18
    -5 2 11 22
    """
    print(fourNumberSum(array, targetSum))  
    
