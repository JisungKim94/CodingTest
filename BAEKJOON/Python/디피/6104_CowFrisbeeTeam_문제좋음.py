import sys
input = sys.stdin.readline
N,F = map(int,input().split())
R = [int(input()) for _ in range(N)]

# 디피디피!! ㅍㅍ!!!!!!!!

def count_teams(N, F, ratings):
    MOD = 100000000

    # dp[i][j] represents the number of ways to choose a team from the first i cows
    dp = [[0] * F for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(F):
            # dp[i-1][j]에다가 N번째 소의 rating을 더하지 않고 그냥 넘어가면 %F가 j가된다.
            # dp[i-1][(j-ratings[i-1]) % F])에다가 N번째 소의 rating을 더하면 %F가 j가된다.
            # 두 케이스를 더하면 N번째 소를 %F했을 때 경우의수가 된다.
            dp[i][j] = (dp[i-1][j] + dp[i-1][(j-ratings[i-1]) % F]) % MOD
    for i in range(len(dp)):
        print(dp[i])
    return (dp[N][0] - 1)%MOD # Subtract 1 to exclude the empty set


print(count_teams(N, F, R))
