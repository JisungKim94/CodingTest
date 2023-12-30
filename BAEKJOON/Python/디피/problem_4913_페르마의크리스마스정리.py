# 1. 걍 소수판별? -> 시간초과
# 2. 에라토스테네스의 체(dp) -> 시간초과
# 3. 체 + 누적합 
# 4. 케이스 놓친게 있었음 primenumber가 2면 p=4c+1 만족 안해도 제곱수로 표현 가능 (1+1)

# 판별 (시간초과)
# def isPrime(num):
#     if num==1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0:
#                 return False
#         return True

# sieve of Eratosthenes
maxnum = 1000001
primes = [True]*maxnum
primes[0] = False
primes[1] = False
for i in range(2,maxnum):
    if primes[i]:
        for j in range(2*i, maxnum, i):
            primes[j] = False

# prefix sum
a = [0]*maxnum # prime
b = [0]*maxnum # is p=4c+1
cnta = 0
cntb = 0
for i in range(maxnum):
    if primes[i]:
        cnta+=1
        if i%4==1:
            cntb+=1
    a[i] = cnta
    b[i] = cntb

# !! 특이한 케이스 2는 1+1로 p=4c+1을 만족하지 않아도 제곱수로 소수표현가능
for i in range(2,maxnum):
    b[i]+=1


while True:
    L, U = map(int, input().split())
    if L == -1 and U == -1:
        break
    
    l = 0 if L<=0 else L
    u = 0 if U<=0 else U
    

    if l>0:
        answer1 = a[u]-a[l-1] # prime
        answer2 = b[u]-b[l-1] # is p=4c+1
    else:
        answer1 = a[u]-a[0] # prime
        answer2 = b[u]-b[0] # is p=4c+1
    
    print(L,U,answer1,answer2)
