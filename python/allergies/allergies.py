from itertools import combinations

allergyList = {
    1: "eggs",
    2: "peanuts",
    4: "shellfish",
    8: "strawberries",
    16: "tomatoes",
    32: "chocolate",
    64: "pollen",
    128: "cats"
}

class Allergies(object):
    """docstring for Allergies."""
    lst = []

    def __init__(self, score):
        for i in range(1, len(allergyList) + 1):
            for comb in combinations(allergyList, i):
                if sum(comb) == score:
                    self.lst = []
                    for allergyID in comb:
                        self.lst.append(allergyList[allergyID])

    def is_allergic_to(self, allergy):
        if allergy in self.lst:
            return True
        else:
            return False
