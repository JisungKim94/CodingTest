import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
W1, W2 = len(word1), len(word2)
dp = [[0]*(W1+1) for _ in range(W2+1)]

# 쫌 생각하기 어려움
for i in range(1,W2+1):
    for j in range(1,W1+1):
        if word2[i-1] == word1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = dp[i][j] + max(dp[i-1][j],dp[i][j-1])

# print(dp)
print(dp[-1][-1])

# # 그나마 쉬움
# dp = [0]*W2
# for i in range(W1):
#     tempmax = 0
#     for j in range(W2):
#         if tempmax < dp[j]:
#             tempmax = dp[j]
#         elif word1[i] == word2[j]:
#             dp[j] = tempmax + 1
# print(max(dp))