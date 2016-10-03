def slices(digitString, substringLength):
    slicesList = []
    if substringLength < 1 or substringLength > len(digitString):
        raise ValueError
    for index, digit in enumerate(digitString):
        templist = []
        if index + substringLength <= len(digitString):
            for i in range(index, index + substringLength):
                templist.append(int(digitString[i]))
            slicesList.append(templist)
    return slicesList
