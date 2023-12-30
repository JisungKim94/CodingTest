# 꼭 반드시 탐색 조건을 아래와 같이 해야 통과한다...
    # if cnt>=C:
    #     l=m+1
    #     answer = m
    # else:
    #     r=m-1
# 그 이유가 뭘까



N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()
# print(home)
l,r = 0,1e11
while l<=r:
    m=(l+r)//2
    cnt = 1
    curr = home[0]
    for i in range(N):
        if curr + m <= home[i]:
            cnt+=1
            curr = home[i]
    # print(l,m,r,cnt)
    if cnt>=C:
        l=m+1
        answer = m
    else:
        r=m-1
print(answer)
# 1 2 4 8 9
