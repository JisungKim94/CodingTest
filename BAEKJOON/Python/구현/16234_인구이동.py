import copy
import sys
sys.setrecursionlimit(10**6)

N,L,R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
move = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def dfs(visited,unions, cr,cc):
    unions[-1].add((cr,cc))
    visited[cr][cc] = 1
    for dr,dc in move:
        nr,nc = cr+dr,cc+dc
        if 0<=nr<N and 0<=nc<N and L<=abs(A[cr][cc]-A[nr][nc])<=R and visited[nr][nc] == 0:
            dfs(visited,unions,nr,nc)
answer = 0
while 1:
    visited_ = copy.deepcopy(visited)
    unions = []
    for i in range(N):
        for j in range(N):
            if visited_[i][j] == 0:
                unions.append(set())
                dfs(visited_, unions, i,j)
    if len(unions) == N*N:
        break
    for u in unions:
        tempsum = 0
        for r,c in u:
            tempsum += A[r][c]
        for r,c in u:
            A[r][c] = tempsum//len(u)
    answer+=1
print(answer)
