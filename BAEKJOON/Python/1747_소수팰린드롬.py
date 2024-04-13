import sys
input = sys.stdin.readline
N = int(input())

# 걍 쉬움

dp = [0]*1000001
for i in range(1,len(dp)):
    for j in range(i,len(dp),i):
        dp[j]+=1
print(dp[:30])
for i in range(N,len(dp)):
    if dp[i]==2 and (i//10):
        temp = str(i)
        print(temp,temp[::-1])
        if temp[::-1] == temp:
            break
