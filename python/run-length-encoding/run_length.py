import re

def encode(phrase):
    encodedPhrase = ""
    charCount = 0
    for key, char in enumerate(phrase):
        charCount += 1
        if key == len(phrase) - 1 or phrase[key+1] != char:
                encodedPhrase += str(charCount) + char if charCount > 1 else char
                charCount = 0
    return encodedPhrase

def decode(phrase):
    decodedPhrase = ""
    for item in re.findall("((?:[0-9]+)?[^0-9])", phrase):
        repeatCount = re.search("([0-9]+)", item)
        repeatChar = re.search("([^0-9])", item)
        if repeatCount:
            for i in range(0, int(repeatCount.group(0))):
                decodedPhrase += repeatChar.group(0)
        else:
            decodedPhrase += repeatChar.group(0)
    return decodedPhrase
