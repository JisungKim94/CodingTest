import sys
input = sys.stdin.readline
import collections

N = int(input().rstrip())
board = []
temp1 = 0
temp2 = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    temp1 = max(temp)
    temp2 = max(temp1,temp2)
    board.append(temp)
# print(temp2)
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0
for giraffe in range(temp2):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and board[i][j]>giraffe:
                stack = collections.deque([(i,j)])
                visited[i][j] = 1
                cnt+=1
        
            while stack:
                cr,cc = stack.popleft()
                for dr,dc in move:
                    nr,nc = cr+dr,cc+dc
                    if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and board[nr][nc]>giraffe:
                        stack.append((nr,nc))
                        visited[nr][nc] = 1
    # print(giraffe,cnt)
    answer = max(answer,cnt)
print(answer)