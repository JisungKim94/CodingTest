import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 걍 단순 그래프 문제

graph = {}
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            graph[i] = graph.get(i,[]) + [j]
        
import collections
start = 0
dist = [[0]*N for _ in range(N)]
for start in range(N):
    visited = [0]*N
    stack = collections.deque([start])
    while stack:
        # print(stack,visited)
        cnode = stack.popleft()
        if graph.get(cnode,0):
            for nnode in graph[cnode]:
                if visited[nnode] == 0:
                    stack.append((nnode))
                    dist[start][nnode] = 1
                    visited[nnode] =  1
for i in dist:
    print(*i)