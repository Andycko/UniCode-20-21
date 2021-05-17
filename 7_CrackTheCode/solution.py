# This challange was basically a ceasar cipher but shifting only letters

# inspired by - https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm

def cipher(input, key):
    result = ""
    for i in range(len(input)):
        char = input[i]
        # Check upper case characters
        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)
        # Check lower case characters 
        elif (97 <= ord(char) <= 122):
            result += chr((ord(char) + key - 97) % 26 + 97)
        # Everything else stays unchanged 
        else:
            result += char
    return result

print(cipher("Zwddg ogjdv!",34))