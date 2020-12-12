def CeaserCipherEncryptor(string, key):
    ciphercharacter_list = list()
    for c in string:
        encryptedcharacterordinal = ord(c) + key
        if encryptedcharacterordinal > 122:
            ciphercharacter_list.append(chr((encryptedcharacterordinal % 122) + 96))
        else:
            ciphercharacter_list.append(chr(encryptedcharacterordinal))

    return ''.join(ciphercharacter_list)


if __name__ == "__main__":
    print(CeaserCipherEncryptor("xyz",2))
