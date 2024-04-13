import sys
import math
input = sys.stdin.readline

# 흠... bfs로 visited 하나 만들어서 진행하면 될거같음
N,M,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

import collections
answer = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            answer+=1
            que = collections.deque([(i,j)])
            visited[i][j] = 1            
            while que:
                cr,cc = que.popleft()
                for dr,dc in move:
                    nr = cr + dr
                    nc = cc + dc
                    if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0 and abs(board[cr][cc] - board[nr][nc])<=K:
                        que.append((nr,nc))
                        visited[nr][nc] = 1
                
print(answer)