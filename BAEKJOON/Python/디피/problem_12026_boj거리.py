import sys
input = sys.stdin.readline
N = int(input())
load = input()
# print(load)

# 약간 투포인터처럼 푸는데 거리 후보들 중에서 적절히 선택해야할듯
# 이렇게 진행하는 제곱?같은 거리문제는 dp도 보통 같이 써야함


dp = [float('inf')]*N
dp[0] = 0
idx = 0
prerange = range(1)
# print(list(prerange))
while 1:
    if load[idx]=='B':
        nextboj = 'O'
    elif load[idx]=='O':
        nextboj = 'J'
    else:
        nextboj = 'B'
    currange = []
    for i in range(idx,N):
        if load[i]==nextboj:
            currange.append(i)
            
    # print(list(prerange),currange)
    for i in prerange:
        for j in currange:
            if j>i:
                dp[j] = min(dp[j],dp[i]+(j-i)**2)
    prerange = currange
    if load[idx] == 'X' or currange == []:
        break
    idx = currange[0]
if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])