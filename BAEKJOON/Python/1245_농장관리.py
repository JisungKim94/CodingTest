import sys
input = sys.stdin.readline
N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 걍 다른문제들 처럼 풀다가 잘 안돼서 오래걸림
# 보통 높이가 높아지거나 낮아지는걸로 탐색을 하는데
# 이 문제는 같은 높이를 탐색하면서 그 주위를 계속 확인하는 식으로 접근해야했다.
# 추가로 visited와 answers 두 가지의 확인용 변수들이 필요했다.

move = [(-1,0), (0,1), (1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
answer = 0
answers = [[0]*M for _ in range(N)]
import collections
for i in range(N):
    for j in range(M):
        if answers[i][j] == 1:
            continue
        que = collections.deque([(i,j)])
        visited = [[0]*M for _ in range(N)]
        height = board[i][j]
        visited[i][j] = 1
        flag = 1
        while que and flag:
            cr,cc = que.popleft()
            for dr,dc in move:
                nr,nc = cr+dr,cc+dc
                if 0<=nr<N and 0<=nc<M:
                    if board[nr][nc] > height:
                        flag = 0
                        break
                    if visited[nr][nc]==0 and board[nr][nc]==height:
                        visited[nr][nc] = 1
                        que.append((nr,nc))
        # print(i,j,que,flag)
        if flag:
            answer+=1
            for r in range(N):
                for c in range(M):
                    if visited[r][c] == 1:
                        answers[r][c] = 1
    
print(answer)
