def CountPairsWithDiff(array, K):
    elements = dict()
    uniquePairsCount = 0
    for item in array:
        elements[item] = None
    
    for item in elements:
        itemDiff = item - K
        itemSum = item + K
        if itemDiff in elements:
            uniquePairsCount += 1
        if itemSum in elements:
            uniquePairsCount += 1
    
    return uniquePairsCount // 2


if __name__ == '__main__':
    print(CountPairsWithDiff([1,7,5,9,2,12,3], 2))
    print(CountPairsWithDiff([9,8,4,0,8,3,6,6,7,3], 3))