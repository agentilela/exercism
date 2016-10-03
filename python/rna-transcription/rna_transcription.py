def to_rna(dnaStrand):
    rnaMap = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    rnaStrand = ""
    for dna in dnaStrand:
        rnaStrand += rnaMap[dna]
    return rnaStrand
