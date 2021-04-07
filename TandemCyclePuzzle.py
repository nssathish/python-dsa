def tandemCyclists(redShirtSpeeds, blueShirtSpeeds, fastest=False):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    maximumSpeed = 0
    for i in range(len(redShirtSpeeds)):
        redShirtSpeed = redShirtSpeeds[len(blueShirtSpeeds) - i - 1] if fastest else redShirtSpeeds[i]
        blueShirtSpeed = blueShirtSpeeds[i]
        maximumSpeed += max(redShirtSpeed, blueShirtSpeed)

    return maximumSpeed


if __name__ == "__main__":
    print(tandemCyclists([5, 5, 3, 9, 2],[3, 6, 7, 2, 1]))
    '''
        2 3 5 5 9
        1 2 3 6 7
    '''
