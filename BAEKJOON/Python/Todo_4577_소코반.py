import sys
input = sys.stdin.readline
R,C = map(int,input().split())
import collections
# 구현문제라고 봐야하지 않을깜..
# 내 위치만 확인하는게 아니고 공의 위치들도 확인하면서 진행하면 될듯 ~!

board = [list(input().split()[0]) for _ in range(R)]
control = list(input())

print(board)
print(control)
balls = []
ends = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 'w' or board[i][j] == 'W':
            start = (i,j)
        if board[i][j] == '+' or board[i][j] == 'W':
            ends.append((i,j))
        if board[i][j] == 'b':
            balls.append((i,j))
for i in range(len(control)):
    control[i]
    
def move(dir,cr,cc):
    if dir == 'U':
        nr,nc = cr-1,cc
        nnr,nnc = cr-2,cc
    elif dir == 'L':
        nr,nc = cr,cc-1
        nnr,nnc = cr,cc-2
    elif dir == 'D':
        nr,nc = cr+1,cc
        nnr,nnc = cr+2,cc
    else:
        nr,nc = cr,cc+1
        nnr,nnc = cr,cc+2
    
    if board[nr][nc] == '#':
        return ((cr,cc),
    elif board[nr][nc] == '.' or board[nr][nc] == '+':
        return (nr,nc)
    elif board[nr][nc] == 'b':
        if board[nnr][nnc] == '.':
