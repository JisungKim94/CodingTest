import sys
input = sys.stdin.readline
n,m = map(int, input().split())
name = [int(input()) for _ in range(n)]

# ... 무슨문젠지 모르겠는데;;
# 알고리즘 분류 보니까 dp문제라네..
# 분류 봐도 어캐풀지 모르겠따 스파...
# 핵싱은 같은 라인에 쓸건지 다음 라인에 쓸건지 dp로 판단하는거
# 걍 보고 배낀 수준이라서 다시 풀어봐야할듯.. 너무어렵다...

dp = [float('inf')]*(n+1)
dp[-1]=0
def giraffe(idx):
    if dp[idx] != float('inf'):
        return dp[idx]
    remains = m-name[idx]
    for i in range(idx+1,n+1):
        if i==n:
            dp[idx]=0
            break
        dp[idx] = min(dp[idx], remains**2 + giraffe(i))
        remains-=(name[i]+1)
        if remains<0:
            break
    return dp[idx]
giraffe(0)
print(dp[0])
# print(dp)
