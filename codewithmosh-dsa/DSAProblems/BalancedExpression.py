from DS.StackOps import Stack


def isBalanced(expression: str) -> bool:
    new_stack = Stack(size = len(expression))
    
    for character in expression:
        if isOpenBracket(character):
            new_stack.push(character)
        elif bracketsMatch(new_stack, character):
            _ = new_stack.pop()
    
    return new_stack.isEmpty()

def bracketsMatch(new_stack: Stack, character: str) -> bool:
    return indexOf(new_stack.peek(), open_brackets()) == indexOf(character, closed_brackets())

def indexOf(character: str, brackets: list) -> int:
    try:
        return brackets.index(character)
    except ValueError as ve:
        return -1

def isOpenBracket(character) -> bool:
    return character in open_brackets()

def open_brackets():
    return ['(', '[', '{', '<']

def closed_brackets():
    return [')', ']', '}', '>']

if __name__ == '__main__':
    expression = '[1234(23+34))'
    print(isBalanced(expression))
    expression = '[1234(23+34)]'
    print(isBalanced(expression))
    expression = '[1234(23+34)<]>'
    print(isBalanced(expression))