def Sieve_of_Eratosthenes(n):
    sieve = [False,False] + [True]*(n-1)  # [True, True .... n개]
    primes = []

    for i in range(2,n+1):
        if sieve[i] == True:
            primes.append(i)
            for j in range(2*i, n+1, i):
                sieve[j] = False

    return primes
    
while (1):
    n = int(input())
    if (n == 0):
        break
    Primes_length = len(Sieve_of_Eratosthenes(2*n)) - len(Sieve_of_Eratosthenes(n))

    print(Primes_length)
