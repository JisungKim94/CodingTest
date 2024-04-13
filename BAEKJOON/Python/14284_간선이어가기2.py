import sys
input = sys.stdin.readline
n,m = map(int,input().split())

# 음... 다익스트라 문제 아닌가?
graph = {}
for i in range(n):
    graph[i+1] = []
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a] += [(b,c)]
    graph[b] += [(a,c)]
s,t = map(int,input().split())

import collections
que = collections.deque([(s,0)])
dist = [float('inf')]*(n+1)
while que:
    cn,ccost = que.popleft()
    
    for (nn,cost) in graph[cn]:
        if ccost+cost < dist[nn]:
            dist[nn] = ccost+cost
            que.append((nn,ccost+cost))
print(dist[t])