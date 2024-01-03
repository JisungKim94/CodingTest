import sys
input = sys.stdin.readline
T = int(input())

# dp로 풀면 될듯...?

dp = [1]*10
predp = dp[::]
answer = [0]*65
answer[1] = 10
for n in range(2,65):
    for i in range(10):
        tmp = 0
        for j in range(10):
            if j<=i:
                tmp+=predp[j]
        dp[i]=tmp
    predp = dp[::]
    answer[n]=sum(dp)
# print(answer)
for _ in range(T):
    n = int(input())
    print(answer[n])
