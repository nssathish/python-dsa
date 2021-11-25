def minNumberOfCoinsToMakeChange(n: int, denoms: list) -> int:
    numberOfCoins = [float("inf")] * (n + 1)
    numberOfCoins[0] = 0

    for denom in denoms:
        for amount in range(n + 1):
            if denom <= amount:
                numberOfCoins[amount] = min(numberOfCoins[amount], numberOfCoins[amount - denom] + 1)

    return -1 if numberOfCoins[n] == float("inf") else numberOfCoins[n]

if __name__ == '__main__':
    print(minNumberOfCoinsToMakeChange(0, [1,5]))
    print(minNumberOfCoinsToMakeChange(7, [1,5]))
    print(minNumberOfCoinsToMakeChange(10, [1, 5, 10, 25]))
    print(minNumberOfCoinsToMakeChange(12, [2, 5, 10]))
    print(minNumberOfCoinsToMakeChange(14, [2, 5, 10]))
    print(minNumberOfCoinsToMakeChange(24, [1, 5, 10]))
    print(minNumberOfCoinsToMakeChange(7, [2, 4]))