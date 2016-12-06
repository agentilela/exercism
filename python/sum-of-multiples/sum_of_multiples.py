def sum_of_multiples(number, factors):
    finalSum = 0
    for i in range(1, number):
        for factor in factors:
            if factor > 0 and i % factor == 0:
                finalSum += i
                break
    return finalSum
