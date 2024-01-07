import sys
input = sys.stdin.readline
N,M = map(int, input().split())
A = [int(input()) for _ in range(N)]

# 투포인터 문제네...

# print(A)
A.sort()
# print(A)
l,r = 0,0
answer = float('inf')
while l<N-1:
    # print(l,r)
    if A[r]-A[l]>=M:
        answer = min(answer,A[r]-A[l])
        l+=1
    else:
        if r<N-1:
            r+=1
        else:
            l+=1
    
    if l==r and r<N-1:
        r+=1
print(answer)