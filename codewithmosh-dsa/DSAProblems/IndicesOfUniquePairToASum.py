def IndicesOfUniquePairToASum(array, targetSum) -> list():
    elementsAndPositions = dict()
    position = 0
    for item in array:
        elementsAndPositions[item] = position
        position += 1
    
    for item in array:
        diff = item - targetSum if item > targetSum else targetSum - item

        if diff in elementsAndPositions:
            return [elementsAndPositions[item], elementsAndPositions[diff]]
    
    return [None, None]


if __name__ == '__main__':
    print(IndicesOfUniquePairToASum([1,7,5,9,2,12,8], 12))
    print(IndicesOfUniquePairToASum([9,8,4,0,3,6], 7))