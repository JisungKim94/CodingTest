import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
move = [(0, 1), (1, 0)]
maxcost = 0

# bfs, dfs 둘 다 메모리 초과 발생
# dp문제구나.. 3차원 dp 하다가 안해도 될거같아서 걍 2차원 dp로 선회

# while stack:
#     (ccost,pre,(cr,cc)) = stack.popleft()
#     # print((ccost,pre,(cr,cc)))
#     if (cr,cc) == (N-1,N-1):
#        maxcost = max(ccost,maxcost) 
#     for dr,dc in move:
#         nr,nc = cr+dr, cc+dc
#         if 0<=nr<N and 0<=nc<N:
#             if board[nr][nc] == (pre+1)%3:
#                 ncost = ccost+1
#             else:
#                 ncost = ccost
#             stack.append((ncost,board[nr][nc],(nr,nc)))
dp = [[0 for _ in range(N)] for _ in range(N)]
# print(dp)
for cr in range(N):
    for cc in range(N):
        dp[cr][cc]=max(dp[cr][cc],dp[cr-1][cc],dp[cr][cc-1])
        if dp[cr][cc]%3 == board[cr][cc]:
            dp[cr][cc]+=1
        # print(dp)

# print(dp)
print(dp[-1][-1])