from sys import stdin
input=stdin.readline
TC = int(input())

move = [(1,0),(0,1),(-1,0),(0,-1)]

for tc in range(TC):
    board=[list(input().rstrip()) for i in range(5)]
    input()
    lenpins = 0
    answer = 0
    for r in range(5):
        for c in range(9):
            if board[r][c] == 'o':
                lenpins+=1
    
    def dfs(cost):
        global answer,lenpins
        pins=[]
        
        for r in range(5):
            for c in range(9):
                if board[r][c] == 'o':
                    pins.append((r,c))
        if len(pins)<lenpins:
            answer=cost
            lenpins=len(pins)
            
        for cr,cc in pins:
            for dr,dc in move:
                pr,pc = cr+dr,cc+dc
                if 0<=pr<5 and 0<=pc<9 and board[pr][pc]=='o':
                    nr,nc = pr+dr, pc+dc
                    if 0<=nr<5 and 0<=nc<9 and board[nr][nc]=='.':
                        # board를 복사하는게 아니고 dfs로 판다음 원복 해 주는게 핵심.. ㅠㅠ
                        board[cr][cc] = '.'
                        board[pr][pc] = '.'
                        board[nr][nc] = 'o'
                        dfs(cost+1)
                        board[cr][cc] = 'o'
                        board[pr][pc] = 'o'
                        board[nr][nc] = '.'
    dfs(0)
    print(lenpins,answer)