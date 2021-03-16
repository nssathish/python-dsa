def GenerateDocument(characters, document):
	ledger = dict()
	for c in document:
		if c not in ledger:
			ledger[c] = 1
		else:
			ledger[c] += 1
	
	print(ledger)
	for c in characters:
		if c in ledger:
			ledger[c] -= 1
		else:
			ledger[c] = -1
	
	print(ledger)
	return len([value for key,value in ledger.items() if value > 0]) == 0


if __name__ == "__main__":
	characters = "A"
	document = "a"
	print(GenerateDocument(characters, document))
	characters = "Bste!hetsi ogEAxpelrt x "
	document = "AlgoExpert is the Best!"
	print(GenerateDocument(characters, document))
