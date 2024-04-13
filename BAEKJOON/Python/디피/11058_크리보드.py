import sys
input = sys.stdin.readline
N = int(input())

# 걍 dp문제인듯
# N = 7인 경우에는 A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V를 눌러 9개를 출력할 수 있다.
# N = 8인 경우에는 A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V, Ctrl-V를 눌러 12개를 출력할 수 있다.
# 그런데.. N = 9인 경우에는 A, A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V, Ctrl-V를 눌러 16개를 출력할 수 있다.
# ?????? 규칙이 안보여잉
# 아예 n+3정도로 끝나는 점화식을 찾으려고 몰두해서 다른쪽 생각을 못 했다.
# 결국 힌트를 봐버렸다 ㅠ
# 복사를 몇 번 하는지에 집중해서 다시 풀어보자

dp = [0] * 101
for i in range(6):
    dp[i] = i+1
idx = 6
while idx<101:
    for i in range(3,idx):
        dp[idx] = max(dp[idx],dp[idx-i]+dp[idx-i]*(i-2))
    idx+=1
# print(dp)
print(dp[N-1])