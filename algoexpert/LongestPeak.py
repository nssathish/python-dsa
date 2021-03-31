def longestPeak(array):
    if len(array) <= 2:
        return 0

    i = 0
    peakLength = 0
    longestPeakLength = 0
    while i < len(array) - 1:
        flat = slopeIncreasing = slopeDecreasing = False
        #print(i)
        while i < len(array) - 1 and array[i] < array[i + 1]:
            slopeIncreasing = True
            i += 1
            peakLength += 1

        while i < len(array) - 1 and array[i] == array[i + 1]:
            flat = True
            i += 1

        #print(f'peaklength after increasing slope: {peakLength}')
        while i < len(array) - 1 and array[i] > array[i + 1]:
            slopeDecreasing = True
            i += 1
            peakLength += 1

        #print(array[i:])
        #print(f'peaklength after decreasing slope: {peakLength}')

        if not flat and slopeIncreasing and slopeDecreasing and peakLength > longestPeakLength:
            longestPeakLength = peakLength

        peakLength = 0
        
    return longestPeakLength + 1 if longestPeakLength > 0 else 0


if __name__ == "__main__":
    print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
    print(longestPeak([5, 4, 3, 2, 1, 2, 1]))
    print(longestPeak([5, 4, 3, 2, 1, 2, 3]))
    print(longestPeak([1, 1, 3, 2, 1]))
