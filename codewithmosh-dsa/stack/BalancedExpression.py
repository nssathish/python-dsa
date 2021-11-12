from StackOps import Stack


def isBalanced(expression):
    new_stack = Stack(len(expression))
    
    open_braces: list = ['(', '[', '{', '<']

    for character in expression:
        if character in open_braces:
            new_stack.push(character)
        elif (character == ')' and new_stack.peek() == '(') or \
            (character == ']' and new_stack.peek() == '[') or \
                (character == '}' and new_stack.peek() == '{') or \
                    (character == '>' and new_stack.peek() == '<'):
            _ = new_stack.pop()
    
    return new_stack.isEmpty()


if __name__ == '__main__':
    expression = '[1234(23+34))'
    print(isBalanced(expression))
    expression = '[1234(23+34)]'
    print(isBalanced(expression))
    expression = '[1234(23+34)<]>'
    print(isBalanced(expression))