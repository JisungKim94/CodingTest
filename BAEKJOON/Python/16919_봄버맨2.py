import sys
input = sys.stdin.readline
R,C,N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
board_all = [['O']*C for _ in range(R)]
board_1 = [['O']*C for _ in range(R)]
board_2 = [['O']*C for _ in range(R)]
if N == 1:
    for i in range(len(board)):
        print(''.join(board[i]))
else:
    if N%2 == 0:
        for i in range(len(board_all)):
            print(''.join(board_all[i]))
    else:
        bomb1 = []
        bomb2 = []
        move = [(0,0), (-1, 0), (0, 1), (1, 0), (0, -1)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    bomb1.append((r,c))
        
        for r,c in bomb1:
            for dr,dc in move:
                nr,nc = r+dr,c+dc
                if 0<=nr<R and 0<=nc<C:
                    board_1[nr][nc] = '.'
        
        for r in range(len(board_1)):
            for c in range(len(board_1[0])):
                if board_1[r][c] == 'O':
                    bomb2.append((r,c))           
        
        for r,c in bomb2:
            for dr,dc in move:
                nr,nc = r+dr,c+dc
                if 0<=nr<R and 0<=nc<C:
                    board_2[nr][nc] = '.'
        if N%4 == 3:
            for i in range(len(board_1)):
                print(''.join(board_1[i]))
        else:
            for i in range(len(board_2)):
                print(''.join(board_2[i]))