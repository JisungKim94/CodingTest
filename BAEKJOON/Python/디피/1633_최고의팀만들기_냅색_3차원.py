import sys
 
skill = []
for line in sys.stdin:skill.append([int(e) for e in line.split()])

# 이거 비슷한문제 프로그래머스에 있던거같은데...
# heap으로 풀어보려 했는데 실패함..
# 0-1 knapsack이란? https://howudong.tistory.com/106
# 0-1 knapsack 문제와 동일하며 weight는 0 value는 skill이라고 볼 수 있다.
# 왜냐면 본질적으로 냅색은 넣냐 마냐의 문제이기 때문이다.
# 이 문제는 배낭이 흰색팀 배낭과 검정팀 배낭이 있으므로 dp의 차수가 하나 증가해야 하는 3차원 dp가 된다.

dp = [[[0 for _ in range(16)]for _ in range(16)]for _ in range(len(skill)+1)]

# 현재 인원을 pass, teamW, teamB에 넣는 경우를 dp에 추가
# dp[i][w][b] 는 i번째 인물까지 탐색한 경우의 백팀 w명 흑팀b명일때의 능력치 최대값
for i in range(len(skill)):
    for w in range(16):
        for b in range(16):
            # 냅색.jpg 보면 거기 있는 파란네모 구간
            if w+1 <= 15:
                dp[i+1][w+1][b] = max(dp[i+1][w+1][b], dp[i][w][b]+skill[i][0])
            if b+1 <= 15:
                dp[i+1][w][b+1] = max(dp[i+1][w][b+1], dp[i][w][b]+skill[i][1])
                
            # 냅색.jpg에 있는 빨간네모 구간
            dp[i+1][w][b] = max(dp[i+1][w][b], dp[i][w][b])

print(dp[-1][15][15])