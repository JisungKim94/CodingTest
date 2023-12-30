import sys
input = sys.stdin.readline

# dp 문제인건 알았으나 쿠폰 행을 만들어야하는 2차원 dp인건 몰랐다..
# 알았더라도 구현을 못 했을듯

N, M = map(int, input().split())
cantgo = list(map(int, input().split()))
# print(cantgo)
days = [0]*(N+1)
for i in cantgo:
    days[i]=1
# print(days)

dp=[[float('inf')]*((N+6)) for _ in range(42)]
day = 0
coupon = 0
dp[day][coupon] = 0 
for day in range(N+1):
    for coupon in range(40):
        if dp[coupon][day] == float('inf'):
            continue
        today = dp[coupon][day]
        if day+1 in cantgo:
            dp[coupon][day+1] = min(dp[coupon][day+1],today)
        if coupon >= 3:
            dp[coupon-3][day+1] = min(dp[coupon-3][day+1],today)
        
        dp[coupon][day+1] = min(dp[coupon][day+1], today + 10000)
        
        for i in range(1,4):
            dp[coupon+1][day+i] = min(dp[coupon+1][day+i], today + 25000)
        for i in range(1,6):
            dp[coupon+2][day+i] = min(dp[coupon+2][day+i], today + 37000)
        
        
# print(dp[0])
answer = float("inf")
for i in range(42):
    answer = min(answer,dp[i][N])
print(answer)
    