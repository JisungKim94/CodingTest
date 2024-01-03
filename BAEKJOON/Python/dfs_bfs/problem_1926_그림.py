import sys
input = sys.stdin.readline
N, M = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 걍 쉬운문제


import collections
sys.setrecursionlimit(10**6)
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
stack = collections.deque([])
visited = [[0]*M for _ in range(N)]

cnt = 0
maxarea = 0
# def dfs(cr,cc):
#     global area
#     for dr,dc in move:
#         nr,nc = cr+dr,cc+dc
#         if 0<=nr<N and 0<=nc<M and board[nr][nc]==1 and visited[nr][nc]==0:
#             visited[nr][nc]=1
#             dfs(nr,nc)
#             area+=1

for i in range(N):
    for j in range(M):
        if visited[i][j]==0 and board[i][j]==1:
            area = 1
            visited[i][j]=1
            # dfs(i,j)
            stack.append((i,j))
            cnt+=1
            while stack:
                (cr,cc) = stack.popleft()
                for dr,dc in move:
                    nr,nc = cr+dr,cc+dc
                    if 0<=nr<N and 0<=nc<M and board[nr][nc]==1 and visited[nr][nc]==0:
                        stack.append((nr,nc))
                        visited[nr][nc]=1
                        area+=1
            maxarea=max(maxarea,area)
print(cnt)
print(maxarea)