def FirstNonRepeatingCharacter(string):
    dictionary = dict()
    result = None

    for c in string:
        if c in dictionary:
            dictionary[c.lower()] += 1
        else:
            dictionary[c.lower()] = 1
    
    for c in string:
        if dictionary[c.lower()] == 1:
            result = c
            break

    return result


if __name__ == '__main__':
    print(FirstNonRepeatingCharacter('A Green apple'))