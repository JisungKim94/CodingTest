import heapq
import collections
import sys

# dfs문제였고 graph 일방향 구현을 하는 부분이 좀 헷갈렸었음
# 그리고 처음엔 heap을 안 썼었는데 ㅅㅣ간초과 났었음

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = collections.defaultdict(list)
oneway = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v, b = map(int, sys.stdin.readline().rstrip().split())
    graph[u] = graph.get(u,[]) + [v]
    graph[v] = graph.get(v,[]) + [u]
    if b == 0:
        oneway[v][u] = 1
k = int(sys.stdin.readline().rstrip())
questions = []
# print(graph)
# print(oneway)

dist = [[float('inf')]*(N+1) for _ in range(N+1)]
for start in range(N+1):
    dist[start][start]=0
    stack = []
    heapq.heappush(stack,(0,start))
    while stack:
        (ccount,cnode) = heapq.heappop(stack)
        if ccount > dist[start][cnode]:
            continue
        for nnode in graph[cnode]:
            if oneway[cnode][nnode]==1:
                if ccount+1 < dist[start][nnode]:
                    dist[start][nnode] = ccount+1
                    heapq.heappush(stack,(ccount+1,nnode))
            else:
                if ccount < dist[start][nnode]:
                    dist[start][nnode] = ccount
                    heapq.heappush(stack,(ccount,nnode))
for _ in range(k):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    print(dist[start][end])