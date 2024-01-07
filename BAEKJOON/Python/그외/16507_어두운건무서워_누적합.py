import sys
input = sys.stdin.readline
R,C,Q = map(int, input().split())
board = [list(map(int, input().rstrip().split())) for _ in range(R)]
pictures = [list(map(int, input().rstrip().split())) for _ in range(Q)]

# 딱 봐도 누적합 문제


prefixboard = [[0]*len(board[0]) for _ in range(len(board))]
for r in range(len(board)):
    for c in range(len(board[0])):
        if c == 0:
            prefixboard[r][c] = board[r][c]
            pre = board[r][c]
        else:
            prefixboard[r][c] = pre + board[r][c]
            pre = prefixboard[r][c]


for r1,c1,r2,c2 in pictures:
    r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
    answer = 0
    for r in range(r1,r2+1):
        if c1 == 0:
            answer += prefixboard[r][c2]-0
        else:
            answer += prefixboard[r][c2]-prefixboard[r][c1-1]
    print(answer//((r2-r1+1)*(c2-c1+1)))
