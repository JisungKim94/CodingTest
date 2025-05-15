import sys
input = sys.stdin.readline
n,m = map(int,input().split())
queens = list(map(int,input().split()))
knight = list(map(int,input().split()))
pawn = list(map(int,input().split()))
board = [[0 for _ in range(m)] for _ in range(n)]

Q,K,P = queens[0],knight[0],pawn[0]
queens = queens[1:]
knight = knight[1:]
pawn = pawn[1:]
for idx in range(0,len(queens),2):
    cr,cc = queens[idx]-1,queens[idx+1]-1
    board[cr][cc] = 2
for idx in range(0,len(knight),2):
    cr,cc = knight[idx]-1,knight[idx+1]-1
    board[cr][cc] = 2
for idx in range(0,len(pawn),2):
    cr,cc = pawn[idx]-1,pawn[idx+1]-1
    board[cr][cc] = 2
# print(board)
moveQ = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
for idx in range(0,len(queens),2):
    ir,ic = queens[idx]-1,queens[idx+1]-1
    for dr,dc in moveQ:
        que = [(ir,ic)]
        while que:
            cr,cc = que.pop()
            board[cr][cc] = 1
            nr,nc = cr+dr, cc+dc
            if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc]!=2:
                que.append((nr,nc))
# print(board)
moveK = [(1+1,1),(1,1+1),(-1-1,1),(-1,1+1),(1+1,-1),(1,-1-1),(-1-1,-1),(-1,-1-1)]
for idx in range(0,len(knight),2):
    cr,cc = knight[idx]-1,knight[idx+1]-1
    for dr,dc in moveK:
        nr,nc = cr+dr, cc+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]):
            board[nr][nc] = 1
# print(board)
    
answer = 0
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == 0:
            answer += 1
print(answer)