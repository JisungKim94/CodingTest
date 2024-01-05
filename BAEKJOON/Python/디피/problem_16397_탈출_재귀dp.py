import sys
input = sys.stdin.readline
N,T,G = map(int, input().split())
# print(N,T,G)

# 이런류 문제들이 좀 있는데 dp였던게 많았떤거 같은디..?
# 왜냐면 최대 T회인데 가능한 조건이 여러개라 조건개수^T 개를 할 순 없으니까
# 근데 이런게 dp index가 커지기만 하면 쉬운데 감소하는것도 같이 있으면 좀 어려워진다 이거처럼...
# 감소하는 문제면 단순히 for문만 돌려서 구할수는 없고 재귀의꼴을 가져야 한다.
# 여기선 stack으로 구현했음

dp = [float('inf')]*(100000)
visited = [0]*(100000)
cur = N
dp[cur] = 0

import collections
stack = collections.deque([cur])
while stack:
    # print(stack)
    cur = stack.popleft()
    if visited[cur] == 1 or dp[cur] == float('inf') or dp[cur]>=T:
        continue
    # buttonA
    visited[cur] = 1
    next = cur + 1
    if 0<=next<len(dp):
        dp[next] = min(dp[next],dp[cur]+1)
        stack.append(next)
    # initialize
    next = cur - 1
    
    # buttonB
    next = cur * 2
    if next == 0:
        pass
    elif next<10:
        next-=1
    elif next<100:
        next-=10
    elif next<1000:
        next-=100
    elif next<10000:
        next-=1000
    elif next<100000:
        next-=10000
    else:
        pass
    
    if 0<=next<len(dp):
        dp[next] = min(dp[next],dp[cur]+1)
        stack.append(next)
# print(dp)
if dp[G]==float('inf'):
    print('ANG')
else:
    print(dp[G])