import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# stack.popleft 로 하면 메모리초과에 시간도 느림 왜일까??


N = int(input().rstrip())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
move = [(1,0),(0,1),(-1,0),(0,-1)]
def dfs(color,board,visited,cr,cc):
    visited[cr][cc] = 1
    for dr,dc in move:
        nr,nc = cr+dr,cc+dc
        if 0<=nr<N and 0<=nc<N and board[nr][nc] == color and visited[nr][nc] == 0:
            dfs(color,board,visited,nr,nc)
def dfs_RG(color,board,visited,cr,cc):
    visited[cr][cc] = 1
    for dr,dc in move:
        nr,nc = cr+dr,cc+dc
        if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0:
            if color == 'R' or color == 'G':
                if board[nr][nc] == 'R' or board[nr][nc] == 'G':
                    dfs_RG(color,board,visited,nr,nc)
            else:
                if board[nr][nc] == board[cr][cc]:
                    dfs_RG(color,board,visited,nr,nc)

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(board[i][j],board,visited,i,j)
            cnt+=1
        else:
            pass

cnt_ = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs_RG(board[i][j],board,visited,i,j)
        else:
            continue
        cnt_+=1

print(cnt, cnt_)