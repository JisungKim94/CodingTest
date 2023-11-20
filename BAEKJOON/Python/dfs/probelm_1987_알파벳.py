import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(map(lambda x:ord(x)-65, input())) for _ in range(R)]
# \n 제거
for i in range(len(board)-1):
    board[i].pop()

visited_alpha = [0] * 26
answer = 1
move = [(1,0), (-1,0), (0,1), (0,-1)]

# print(board)

def dfs(visited_alpha, board, cost, cr, cc):
    global answer
    answer = max(cost,answer)
    visited_alpha[board[cr][cc]]=1
    for dr,dc in move:
        nr,nc = cr+dr, cc+dc
        # print(cr,cc,nr,nc, visited_alpha)
        if 0<= nr < R and 0<= nc < C and visited_alpha[board[nr][nc]]==0:
            # print(cr,cc,nr,nc, visited_alpha)
            dfs(visited_alpha, board, cost+1, nr, nc)
            # dfs 파고들때는 visited 0 처리를 안 해야하고 이쪽 길 포기했을 때는 0 처리 해야함
            # 즉 아래와 같이 구현
            visited_alpha[board[nr][nc]]=0

dfs(visited_alpha, board, answer, 0, 0)
# print(visited_alpha)
print(answer)