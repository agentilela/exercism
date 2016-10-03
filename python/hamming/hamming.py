def distance(strand1, strand2):
    distance = 0
    for index, value in enumerate(strand1):
        if value != strand2[index]:
            distance += 1
    return distance
