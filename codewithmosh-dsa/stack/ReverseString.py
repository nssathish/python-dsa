from StackOps import Stack


def string_reverse(string: str) -> str:
    _stack = Stack(len(string))
    for character in string:
        _stack.push(str(character))
    
    result = [_stack.pop() for i in range(len(_stack.stack))]

    return "".join(result)


if __name__ == '__main__':
    print(string_reverse("sathish kumar"))