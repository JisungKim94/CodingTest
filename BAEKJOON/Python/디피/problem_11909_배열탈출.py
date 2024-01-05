import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[float('inf') for _ in range(n)] for _ in range(n)]
# print(board)
dp[0][0] = 0
for cr in range(n):
    for cc in range(n):
        if 0 <= cr < n and 0 <= cc < n:
            if board[cr][cc] < board[cr][cc-1]:
                dp[cr][cc] = min(dp[cr][cc],dp[cr][cc-1])
            else:
                dp[cr][cc] = min(dp[cr][cc],dp[cr][cc-1]+(board[cr][cc]-board[cr][cc-1]+1))

            if board[cr][cc] < board[cr-1][cc]:
                dp[cr][cc] = min(dp[cr][cc],dp[cr-1][cc])
            else:
                dp[cr][cc] = min(dp[cr][cc],dp[cr-1][cc]+(board[cr][cc]-board[cr-1][cc]+1))

print(dp[-1][-1])


# 시간초과
# move = [(1, 0), (0, 1)]
# cost = float('inf')
# def dfs(ccost,cr,cc):
#     global cost
#     if (cr,cc) == (n-1,n-1):
#         cost = min(ccost,cost)
#     else:
#         for dr, dc in move:
#             nr, nc = cr + dr, cc + dc
#             if 0 <= nr < n and 0 <= nc < n:
#                 if board[cr][cc]>board[nr][nc]:
#                     dfs(ccost,nr,nc)
#                 else:
#                     dfs(ccost+(board[nr][nc]-board[cr][cc]+1),nr,nc)
# dfs(0,0,0)
# print(cost)

# 메모리초과
# stack = collections.deque([(0,(0,0))])
# while stack:
#     ccost,(cr, cc) = stack.popleft()
#     if (cr,cc) == (n-1,n-1):
#         cost = min(ccost,cost)
#         continue
#     for dr, dc in move:
#         nr, nc = cr + dr, cc + dc
#         if 0 <= nr < n and 0 <= nc < n:
#             if board[cr][cc]>board[nr][nc]:
#                 stack.append((ccost,(nr,nc)))
#             else:
#                 stack.append((ccost+(board[nr][nc]-board[cr][cc]+1),(nr,nc)))
# print(cost)