from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
visited = [[0] * M for _ in range(N)]

move = [(-1,0), (1,0), (0,-1), (0,1)]

def check(nr, nc, i):
    if i == 0:
        dr = 0
        for dc in range(W):
            if board[nr+dr][nc+dc] == 1:
                return False
    elif i == 1:
        dr = H-1
        for dc in range(W):
            if board[nr+dr][nc+dc] == 1:
                return False
    elif i == 2:
        dc = 0
        for dr in range(H):
            if board[nr+dr][nc+dc] == 1:
                return False
    else:
        dc = W-1
        for dr in range(H):
            if board[nr+dr][nc+dc] == 1:
                return False
    return True

flag = True
stack = deque([(0, Sr-1, Sc-1)])
while stack:
    ccost, cr, cc = stack.popleft()
    visited[cr][cc] = True

    if cr == Fr-1 and cc == Fc-1:
        print(ccost)
        flag = False
        break

    for i,(dr,dc) in enumerate(move):
        nr,nc = cr + dr, cc +dc
        if 0<=nr<N and 0<=nc<M and 0<=(nr+H-1)<N and 0<=(nc+W-1)<M\
            and not visited[nr][nc] and check(nr,nc,i):
            visited[nr][nc] = 1
            stack.append((ccost+1,nr,nc))
if flag:
    print(-1)