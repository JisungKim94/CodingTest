import sys
input = sys.stdin.readline
A,B = map(int,input().split())
# 누적합 근데 1일때는 예외처리해야함
if A == 1:
    pass
else:
    A-=1

# dp
dp = [(1,1),(3,2),(8,4)]
for i in range(3,51):
    j = i-2
    temp = 2**i + dp[-1][0]
    while j>=0:
        temp+=dp[j][0]
        j-=1
    dp.append((temp,2**i))
# print(dp)

for i in range(len(dp)):
    if 2**i>B:
        tempB = i-1
        break
    if 2**i>A:
        continue
    tempA = i
answerA,answerB = dp[tempA][0],dp[tempB][0]

# dp 이용하기
# 2의 제곱수에 가까운 값 구하기
i=1
while 1:
    if 2**i>A:
        a = i-1
        break
    i+=1
i=1
while 1:
    if 2**i>B:
        b = i-1
        break
    i+=1
# print(A,B)

# 짤짤이 구하기 (dp를 이용)
# print(leftA,leftB)
leftA,leftB = A-2**a,B-2**b
i=0
while leftA != 0:
    for i in range(len(dp)):
        if dp[i][1]>=leftA:
            break
    if dp[i][1]==leftA:
        answerA+=dp[i][0]
        leftA -= dp[i][1]
    else:
        answerA+=dp[i-1][0]
        leftA -= dp[i-1][1]
i=0
while leftB != 0:
    for i in range(len(dp)):
        if dp[i][1]>=leftB:
            break
    if dp[i][1]==leftB:
        answerB+=dp[i][0]
        leftB -= dp[i][1]
    else:
        answerB+=dp[i-1][0]
        leftB -= dp[i-1][1]
# print(answerA,answerB)
if A == 1:
    answerA = 0
print(answerB-answerA)


# 1
# 2
# 1 4 
# 1 2 1 8
# 1 2 1 4 1 2 1 16
# 1 2 1 4 1 2 1 8 1 2 1 4 1 2 1 32
# 1 2 1 4 1 2 1 8 1 2 1 4 1 2 1 16  1 2 1 4 1 2 1 8 1 2 1 4 1 2 1 64 
# 1 2 1 4 1 2 1 8 1 2 1 4 1 2 1 16 1 2 1 4 1 2 1 8 1 2 1 4 1 2 1 32  1 2 1 4 1 2 1 8 1 2 1 4 1 2 1 16 1 2 1 4 1 2 1 8 1 2 1 4 1 2 1 128

# 1
# 2
# 1 4
# [1] [0] 8
# [2] [1] [0] 16
# [3] [2] [1] [0] 32
# [16] [8] [4] [2] [1] 64
# ...
