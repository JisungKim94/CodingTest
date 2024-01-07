import sys
input = sys.stdin.readline
N = int(input())
answer = 0
dots = []
for _ in range(N):
    dots.append(tuple(map(int, input().split())))
dots.sort()
# print(dots)
dp = [1]*N
# 왼쪽에 정렬한 전봇대가 있다고 할 때
# r1<r2 인 그림만 존재한다면 겹치는 전깃줄이 없다고 볼 수 있다.
# 즉 전깃줄이 겹치지 않으려면 위 조건을 만족하게 오른쪽 전봇대를 선택하는 문제가 되고
# 그 문제는 오른쪽 전봇대의 가장 긴 증가하는 부분수열(LIS, 일부 원소만 골랐을 때 그 원소가 항상 증가하는 수열)
# 구하는 문제와 같다. 우리가 구한 dp는 겹치지 않는 경우를 구한거니까 마지막에 N에서 dp max를 빼주면 된다.
# https://chanhuiseok.github.io/posts/algo-49/
# LIS 기본꼴
# dp = [1]*n
# for i in range(n):
#     for j in range(i):
#         if arr[j]<arr[i]:
#             dp[i] = max(dp[i],dp[j]+1)
# j번째 원소에 내껄(i번원소) 붙일 수 있는지 확인하고 가능하면 그게 max인지 확인하는 과정
        
for i in range(N):
    for j in range(i):
        if dots[i][1]>dots[j][1]:
            dp[i]=max(dp[j]+1,dp[i])
        # print(dp)
print(N-max(dp))