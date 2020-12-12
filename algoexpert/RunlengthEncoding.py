def RunlengthEncode(string):
    i = -1
    encodedString = list()
    while i < len(string) - 1:
        i += 1
        textLength = 1

        while i < len(string) - 1 and string[i] == string[i + 1]:
            textLength += 1
            if textLength % 9 == 0:
                encodedString.append('9' + string[i])
                textLength %= 9

            i += 1
        else:
            if textLength % 9 != 0:
                encodedString.append(str(textLength) + string[i])

    return ''.join(encodedString)


if __name__ == "__main__":
    print(RunlengthEncode("ABCDEFGHH")) #1A1B1C1D1E1F1G2H
    print(RunlengthEncode("AAAAAAAAAAAABBBBAADDDABB")) #9A3A4B2A3D1A2B
    print(RunlengthEncode("A")) #1A
    print(RunlengthEncode("************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"))
    print(RunlengthEncode("                          "))
    print(RunlengthEncode("aaaaaaaaa"))
    print(RunlengthEncode("........______=========AAAA   AAABBBB   BBB"))
