import re

def word_count(sentence):
    wordCount = {}
    for word in re.findall(r"([^\W_]+)", sentence.lower()):
        wordCount[word] = wordCount.get(word, 0) + 1
    return wordCount
