from StackOps import Stack


def isBalanced(expression: str) -> bool:
    new_stack = Stack(len(expression))
    
    for character in expression:
        if isOpenBracket(character):
            new_stack.push(character)
        elif bracketsMatch(new_stack, character):
            _ = new_stack.pop()
    
    return new_stack.isEmpty()

def bracketsMatch(left: str, right: str) -> bool:
    return (character == ")" and new_stack.peek() == "(") or \
            (character == ']' and new_stack.peek() == "[') or \
                (character == '}' and new_stack.peek() == '{') or \
                    (character == '>' and new_stack.peek() == '<')
 
 def indexOf(character)

def isOpenBracket(character) -> bool:
    return character in open_brackets()

def open_brackets():
    return ['(', '[', '{', '<']


if __name__ == '__main__':
    expression = '[1234(23+34))'
    print(isBalanced(expression))
    expression = '[1234(23+34)]'
    print(isBalanced(expression))
    expression = '[1234(23+34)<]>'
    print(isBalanced(expression))