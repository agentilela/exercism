def sieve(number):
    sievList = []
    A = [True] * (number + 1)
    A[0] = A[1] = False
    for (i, isPrime) in enumerate(A):
        if isPrime:
            for n in xrange(i*i, number + 1, i):
                A[n] = False
            sievList.append(i)
    return sievList
