import sys
input = sys.stdin.readline
M,N = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
# print(info)

import collections
sys.setrecursionlimit(10**6)
move = [(-1,0), (0,1), (1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
visited = [[0]*N for _ in range(M)]

stack = collections.deque([])
answer = 0
def dfs(cr,cc,info,visited):
    for dr,dc in move:
        nr,nc = cr+dr,cc+dc
        if 0<=nr<M and 0<=nc<N and visited[nr][nc]==0 and info[nr][nc]==1:
            visited[nr][nc]=1
            dfs(nr,nc,info,visited)

for r in range(M):
    for c in range(N):
        if visited[r][c]==0 and info[r][c]==1:
            dfs(r,c,info,visited)
            answer+=1

print(answer)