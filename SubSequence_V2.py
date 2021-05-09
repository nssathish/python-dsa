def main():
    V = input()
    numberOfComposition = int(input())
    B = [input() for _ in range(numberOfComposition)]

    for composition in B:
        if test(V, composition) and len(composition) <= len(V):
            print('POSITIVE')
        else:
            print('NEGATIVE')

def test(V, composition):
    sequenceIndex = 0
    compositionIdx = 0
    found = False

    while compositionIdx < len(composition) and sequenceIndex < len(V):
        c = composition[compositionIdx]
        if c == V[sequenceIndex]:
            compositionIdx += 1
            sequenceIndex += 1
            found = True
        else:
            sequenceIndex += 1
            found = False

    return found

if __name__ == "__main__":
    main()
