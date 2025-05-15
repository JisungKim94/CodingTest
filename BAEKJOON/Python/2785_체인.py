import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))

PA = 1
for i in A:
    PA *= i

B = []
cnt = 1
while N-cnt >= 0:
    PB = 1
    if B:
        for i in B:
            PB *= i    
        PB = PB*9**(N-cnt)
    else:
        PB = 9**(N-cnt)
    # print(cnt,PB)
    for i in range(1,10):
        if PB*i > PA:
            # print(PB*i, PB,i)
            B.append(i)
            break
    cnt+=1
# print(B)
if B:
    print(*B)
else:
    print(-1)