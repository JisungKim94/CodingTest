import sys
input = sys.stdin.readline
N,K = map(int, input().split())


# 음... 무슨문제지;; bfs??? 그냥 수학?? 이분(삼분)탐색? dp?
# 걍 bfs 문제였음.. visited = cost+1 부분 못풀었었음


# dp = [100000]*(K+1)
# dp[N] = 0
# # for idx in range(len(dp)-1):
# idx=0
# pre = dp[0]
# while 0<=idx<len(dp)-1:
#     dp[idx+1] = min(dp[idx+1],dp[idx]+1)
#     dp[idx-1] = min(dp[idx-1],dp[idx]+1)
#     if 2*idx<len(dp):
#         dp[2*idx] = min(dp[2*idx],dp[idx]+1)
    
#     # print(idx,dp)
#     preK = dp[K]
#     if pre!=dp[idx-1] and idx>0:
#         idx-=1
#     else:
#         pre = dp[idx]
#         idx+=1
# print(dp[K])

import collections
stack = collections.deque([(0,N)])
mincost = float('inf')
answer = 0
MAX = 100001
# visited = [0]*(K+N+1)
visited = [0]*(2*MAX+1)
while stack:
    ccost,cnode = stack.popleft()
    if ccost>mincost:
        continue
    if cnode==K:
        mincost=min(mincost,ccost)
        if ccost==mincost:
            answer+=1
        
    
    if 0<=cnode*2<(2*MAX-1) and (visited[cnode*2] == 0 or visited[cnode*2]==ccost+1):
        stack.append((ccost+1,cnode*2))
        visited[cnode*2]=ccost+1
    if 0<=cnode+1<=(MAX-1) and (visited[cnode+1] == 0 or visited[cnode+1]==ccost+1):
        stack.append((ccost+1,cnode+1))
        visited[cnode+1]=ccost+1
    if 0<=cnode-1<(MAX-1) and (visited[cnode-1] == 0 or visited[cnode-1]==ccost+1):
        stack.append((ccost+1,cnode-1))
        visited[cnode-1]=ccost+1
        
print(mincost)
print(answer)