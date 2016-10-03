def encode(phrase):
    encodedString = ""
    charCounter = 0
    for char in phrase.lower():
        if charCounter == 5:
            encodedString += " "
            charCounter = 0
        if ord(char) in range(97, 123): # A-Z
            encodedString += chr(219 - (ord(char)))
            charCounter += 1
        elif ord(char) in range(48, 58): # 0-9
            encodedString += char
            charCounter += 1
    return encodedString.strip()

def decode(phrase):
    decodedString = ""
    for char in phrase:
        if ord(char) in range(97, 123):
            decodedChar = chr(219 - (ord(char)))
            decodedString += decodedChar
    return decodedString
