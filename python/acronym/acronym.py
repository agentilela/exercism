import re


def abbreviate(phrase):
    abv = ""
    for word in re.findall(r"(?:[a-z])([A-Z])|(?:^| |-)(\w)", phrase):
        for acronym in word:
            if acronym != '':
                abv += acronym
    return abv.upper()
