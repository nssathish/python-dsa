def NumberOfWaysOfCoinsToGetTargetAmount(denominations, targetamount):
    ways = [0] * (targetamount + 1)
    # because if the amount is 0 and the denominations are not-empty then it can be arrived in 1 way
    # (by not using any coins)
    ways[0] = 1
    '''
    1. initialize an array that is the size of the amount + 1
        - each index represents the sub-sum of the actual amount
    2. first element will be 1 ie., array[0] = 1
        - index 0 is the target amount, when 0, it can be formed by no coins that is 1 way.
        - So the no.of ways = 1
    3. loop the denominations to every amount between 0 and the target amount (index 0 to targetamount)
    4. go till amount == taken denomination
    5. ways[amount] += ways[amount - denom]
    '''

    for denomination in denominations:
        for amount in range(targetamount + 1):
            if denomination <= amount:
                ways[amount] += ways[amount - denomination]

    return ways[targetamount]



if __name__ == '__main__':
    print(NumberOfWaysOfCoinsToGetTargetAmount([1, 2, 5, 10, 25], 10))
    print(NumberOfWaysOfCoinsToGetTargetAmount([1, 5, 10, 25], 10))
    print(NumberOfWaysOfCoinsToGetTargetAmount([1, 5], 6))
