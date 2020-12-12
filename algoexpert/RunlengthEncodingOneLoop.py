def RunlengthEncode(string):
	encodedString = list()
	currentRunLength = 1
	for i in range(len(string) - 1):
		currentChar = string[i]
		nextChar = string[i + 1]
		
		if currentChar != nextChar or currentRunLength == 9:
			encodedString.append(str(currentRunLength))
			encodedString.append(currentChar)
			currentRunLength = 0
		
		currentRunLength += 1

	encodedString.append(str(currentRunLength))
	encodedString.append(string[len(string) - 1])

	return ''.join(encodedString)


if __name__ == "__main__":
    print(RunlengthEncode("ABCDEFGHH")) #1A1B1C1D1E1F1G2H
    print(RunlengthEncode("AAAAAAAAAAAABBBBAADDDABB")) #9A3A4B2A3D1A2B
    print(RunlengthEncode("A")) #1A
    print(RunlengthEncode("************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"))
    print(RunlengthEncode("                          "))
    print(RunlengthEncode("aaaaaaaaa"))
    print(RunlengthEncode("........______=========AAAA   AAABBBB   BBB"))
