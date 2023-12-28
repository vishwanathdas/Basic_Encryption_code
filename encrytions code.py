def encryption(string, step):
    output = ""
    for char in string:
        output += chr(ord(char) - step)
    return output

def decryption(string, step):
    output = ""
    for char in string:
        output += chr(ord(char) + step)
    return output

if __name__ == "__main__":
    string = "Encrypt me!"
    step = 2
    encrypted = encryption(string, step)
    decrypted = decryption(encrypted, step)
    print(f"Original: {string}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
