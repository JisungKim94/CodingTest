import sys
input = sys.stdin.readline
# 한 번 꼬은 이분탐색일듯

N,K = map(int, input().split())
days = list(map(int, input().split()))
l,r = 1,10**10
while l<=r:
    m = (l+r)//2
    # print(l,m,r)
    idx = 1
    total = 0
    total_0 = 0
    total_1 = 0
    while idx<len(days):
        n = (days[idx]-days[idx-1])
        if n>m:
            n=m
        else:
            pass
        
        total_0 = m*n
        if n%2 == 0:
            total_1 = (n//2)*(0+n-1)
        else:
            total_1 = (n//2)*(0+n-1) + (n-1)//2
        total += total_0 - total_1
        idx+=1

    total_0 = m*m
    if m%2 == 0:
        total_1 = (m//2)*(0+m-1)
    else:
        total_1 = (m//2)*(0+m-1) + (m-1)//2
    total += total_0 - total_1
    
    if total == K or l==r==m:
        break
    elif total>K:
        r=m
    else:
        l=m+1

print(m)
