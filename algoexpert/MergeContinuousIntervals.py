def mergeContinuousIntervals(intervals):
    #[[1,2], [3, 5], [4, 7], [6, 8], [9, 10]]
    #
    #ANSWER: [[1,2],[3, 8], [9, 10]]

    result = list()
    i = 0
    while i < len(intervals):
        resultInterval = intervals[i]

        while i < len(intervals) - 1:
            nextInterval = intervals[i + 1]
            if resultInterval[1] >= nextInterval[0]:
                resultInterval = [resultInterval[0], nextInterval[1]]
#                print(f'inside while: {resultInterval}')
#                print(f'inside while: {i}')
                i += 1
            else:
#                print(f'inside else: {i}')
                break

#        print(resultInterval)
        result.append(resultInterval)
        i += 1

    return result


if __name__ == "__main__":
    print(mergeContinuousIntervals([[1,2], [3, 5], [4, 7], [6, 8], [9, 10]]))
