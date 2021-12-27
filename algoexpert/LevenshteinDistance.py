def calculate_levenshtein_distance(source, target):
    result = calculatedistances(source, target)
    return result[len(source)][len(target)]

def calculatedistances(source, target):
    distances = list()
    rows = len(source) + 1
    columns = len(target) + 1

    for i in range(rows):
        if i == 0:
            distances.append([element for element in range(columns)])
        else:
            distances.append([ 0 ] * columns)
            distances[i][0] = i

    for i in range(1, rows):
        for j in range(1, columns):
            '''
                0 0 0 0 0
                0 0 0 0 0
                0 0 0 0 0
                0 0 0 0 0
            '''
            if source[i - 1] == target[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                rowDeleteDistance = distances[i - 1][j]
                colDeleteDistance = distances[i][j - 1]
                previousDistance = distances[i - 1][j - 1]
                distances[i][j] = min(rowDeleteDistance, colDeleteDistance, previousDistance) + 1

        print(distances)

    return distances


if __name__ == '__main__':
    print(calculate_levenshtein_distance('abc', 'yabd'))
    print(calculate_levenshtein_distance('abd', 'yabd'))
    print(calculate_levenshtein_distance('', ''))