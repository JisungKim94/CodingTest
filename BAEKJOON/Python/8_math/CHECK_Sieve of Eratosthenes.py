# =============================
# Sieve of Eratosthenes
# https://wikidocs.net/21638
# 
# a = [1, 3] + [2] * 1
# result : a = [1, 3, 2]
# =============================
n = int(input())

sieve = [False,False] + [True]*(n-1)
primes = []

for i in range(2,n+1):
    if sieve[i] == True:
        primes.append(i)
        for j in range(2*i, n+1, i):
            sieve[j] = False

print(primes)        
print(len(primes))

# 함수꼴

""" 
def Sieve_of_Eratosthenes(n):
    sieve = [False,False] + [True]*(n-1)  # [True, True .... n개]
    primes = []

    for i in range(2,n+1):
        if sieve[i] == True:
            primes.append(i)
            for j in range(2*i, n+1, i):
                sieve[j] = False

    return primes
"""