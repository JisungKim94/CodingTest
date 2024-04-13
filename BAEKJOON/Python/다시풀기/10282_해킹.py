import sys
input = sys.stdin.readline
TC = int(input())

# s는 간선간 비용이고 그거의 최소값을 구하면 될거같은데..
# 다익스트라??

import collections
for _ in range(TC):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    que = collections.deque([(0,c)])
    dist = [float('inf')]*(n+1)
    dist[c] = 0
    
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))
    while que:
        # print(que)
        ccost,cnode = que.popleft()    
        
        for nnode,cost in graph[cnode]:
            ncost = ccost+cost
            if dist[nnode]>ncost:
                dist[nnode]=ncost
                que.append((ncost,nnode))
    # print(dist)
    answer1 = 0
    answer2 = 0
    for di in dist:
        if di != float('inf'):
            answer1+=1
            answer2 = max(answer2,di)
    print(answer1,answer2)  