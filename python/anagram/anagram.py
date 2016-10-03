def detect_anagrams(checkWord, wordList):
    anagramList = []
    for word in wordList:
        if sorted(word.lower()) == sorted(checkWord.lower()) and word.lower() != checkWord.lower():
            anagramList.append(word)
    return anagramList
