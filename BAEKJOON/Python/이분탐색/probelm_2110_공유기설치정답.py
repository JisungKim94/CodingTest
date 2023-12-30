N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()

start,end = 1,home[-1]-home[0]
answer = 0
while start<=end:
    middle = (start+end)//2
    curr = home[0]
    cnt = 1
    
    for i in range(1,len(home)):
        if curr+middle <= home[i]:
            cnt+=1
            curr = home[i]
    if cnt>=C:
        answer=middle
        start=middle+1
    else:
        end=middle-1
print(answer)