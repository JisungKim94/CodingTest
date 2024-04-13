import sys
input = sys.stdin.readline
N,M = map(int, input().split())
A = list(map(int, input().split()))
A[-1] = 0
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,t = map(int, input().split())
    if A[a]==1 or A[b]==1:
        continue
    graph[a].append((b, t))
    graph[b].append((a, t))
# print(graph)

# dijkstra 문제인가..?
# >> 시간초과
# >> 조건추가 (if ccost > dist[cnode] or cnode == N-1: continue)
# >> 시간초과
# >> 결국 답을 봤는데 graph를 dictionary로 만들어서 그런거였음...
# >> 메모리 아끼려는 생각이었는데 속도 차이가 많이 나나보ㅓ다
import heapq
que = []
heapq.heappush(que,(0,0))
dist = [float('inf')]*N
dist[0] = 0
visited = [0]*N
while que:
    ccost,cnode = heapq.heappop(que)
    if visited[cnode] == 1:
        continue
    visited[cnode] = 1
    if ccost > dist[cnode] or cnode == N-1:
        continue
    for nnode,dcost in graph[cnode]:
        ncost = ccost+dcost
        if ncost < dist[nnode]:
            dist[nnode] = ncost
            heapq.heappush(que,(ncost,nnode))
if dist[-1] == float('inf'):
    print(-1)
else:
    print(dist[-1])