K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
# print(lines)

l,r = 1,2**31
while l<=r:
    mid = (l+r)//2
    n = 0
    for line in lines:
        n+=line//mid
    
    if n<N:
        r=mid-1
    else:
        l=mid+1
mid = (l+r)//2
print(mid)
