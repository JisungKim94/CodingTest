import sys
input = sys.stdin.readline
n,t = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(n)]
# print(problems)

# 걍 bfs 문제 아닐까..?
# 아dp 문제구나
# 아니네 같은 소요시간이 이씅면 dp로 풀수가없음
# dfs에다가 cnt적용 : 시간초과
# 2차원 dp를 써야할듯.. knapsack이네..

dp = [[0]*(t+1) for _ in range(n)]
for time in range(problems[0][0],t+1):
    dp[0][time] = problems[0][1]
for numb in range(1,n):
    for time in range(t+1):
        if time-problems[numb][0]>=0:
            dp[numb][time] = max(dp[numb-1][time],dp[numb-1][time-problems[numb][0]]+problems[numb][1])
        else:
            dp[numb][time] = dp[numb-1][time]
print(max(dp[-1]))