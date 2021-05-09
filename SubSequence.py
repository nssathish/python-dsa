def main():
    V = input()
    sequenceLength = len(V)
    numberOfCompositions = int(input())
    B = [input() for _ in range(numberOfCompositions)]

    for composition in B:
        if test(V, composition) and len(composition) <= sequenceLength:
            print('POSITIVE')
        else:
            print('NEGATIVE')


def test(V, composition):
    sequenceIndex = 0
    compositionIndex = 0
    sequenceLength = len(V)
    found = False

    for c in composition:
        while sequenceIndex < sequenceLength and c != V[sequenceIndex]:
            sequenceIndex += 1
        else:
            if sequenceIndex < sequenceLength and c == V[sequenceIndex]:
                found = True
            elif sequenceIndex == sequenceLength:
                found = False
        sequenceIndex += 1

    return found

if __name__ == "__main__":
    main()
