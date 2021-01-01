import stackusingarray.ArrayStack

def reverse_file(filename):
	S = stackusingarray.ArrayStack.ArrayStack()
	
	original = open(filename)
	for line in original:
		S.push(line.strip('\n'))
	original.close()

	output = open(filename, 'w+')
	while not S.is_empty():
		output.write(S.pop() + '\n')
	output.close()


if __name__ == "__main__":
	reverse_file('/Users/suchithradhanaraj/python-dsa/stack/reverse_file')
