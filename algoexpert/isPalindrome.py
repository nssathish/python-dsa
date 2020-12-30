def isPalindrome(string, n=None):
    if n is None:
        n = 0
    elif n >= len(string):
        return ""

    isPalindrome(string, n + 1)
    print(string[n])

if __name__ == "__main__":
    print(isPalindrome("sathish"))
