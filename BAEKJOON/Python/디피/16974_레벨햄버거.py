N,X = map(int, input().split())

# 구간을 나눠서 진행 시켜야 함
# 총 5구간이 나옴 B 이전 P 이전 B


# 0 = P = 0,1 1
# 1 = B P P P B = 131 = 2,3 5
# 2 = B BPPPB P BPPPB B = 6,7 13
# 3 = B BBPPPBPBPPPBB P BBPPPBPBPPPBB B = 14,15 29  
# 4 = 4 31113212311133 1 331113212311134 = 30,31 61
dp = [(0,1)]
for i in range(1,N+1):
    buger,pattie = dp[i-1][0],dp[i-1][1]
    dp.append((buger*2+2, pattie*2+1))
# print(dp)
# print(dp[50])
level = N
idx = X
answer = 0
while level>=0:
    # print(level,idx,answer)
    if idx==1:
        if level == 0:
            answer+=1
        else:
            answer += 0
        break
    elif idx==sum(dp[level]):
        answer += dp[level][1]
        break
    elif idx==sum(dp[level])//2+1:
        answer += dp[level][1]//2+1
        break
    else:
        if idx<=sum(dp[level])//2:
            level-=1
            idx-=1
        else:
            answer+=dp[level-1][1]+1
            idx-=(sum(dp[level-1])+2)
            level-=1
# print(level,idx,answer)
print(answer)