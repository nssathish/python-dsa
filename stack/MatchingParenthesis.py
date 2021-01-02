import stackusingarray.ArrayStack

def is_matched(string):
    left = '({['
    right = ')}]'
    S = stackusingarray.ArrayStack.ArrayStack()

    for c in string:
        if c in left:
            S.push(c)
        elif c in right:
            if S.is_empty():
                return False
            elif right.index(c) != left.index(S.pop()):
                return False

    return S.is_empty()


if __name__ == "__main__":
    string = '(((((){})[()])())[])'
    print(is_matched(string))
    string = '(((()'
    print(is_matched(string))
