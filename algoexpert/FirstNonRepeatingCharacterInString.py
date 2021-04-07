def findNonRepeatingCharacterInString(string):
    store = {}
    for c in string:
        if c not in store:
            store[c] = 1
        else:
            store[c] += 1

    for i in range(len(string)):
        c = string[i]
        if store[c] == 1:
            return i

    return -1


if __name__ == "__main__":
    print(findNonRepeatingCharacterInString("abcdcaf"))
    print(findNonRepeatingCharacterInString("aacdafc"))
