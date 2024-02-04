import sys
input = sys.stdin.readline

# bfs,dfs인데 구현이 빡센문제인가..?
# 그러하다

N,M,P = map(int, input().split())
S = list(map(int, input().split()))
board = [list(input().rstrip()) for _ in range(N)]

move = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[0]*M for _ in range(N)]
import collections
ques = [collections.deque([]) for _ in range(P)]
visitedcnt = 0
flag = 1 # 더이상 이동 불가한 케이스 구분용
for r in range(N):
    for c in range(M):
        if visited[r][c] == 0 and board[r][c] == '#':
            visited[r][c] = 1
            visitedcnt+=1
            
        if visited[r][c] == 0 and board[r][c] != '.':
            cnt = int(board[r][c])
            ques[cnt-1].append((S[cnt-1],(r,c)))
            visited[r][c]=1
# print(ques)
flag = 1
while flag:
    flag = 0
    cnt = 0
    for que in ques:
        cnt+=1
        if len(que)>0:
            flag = 1
        tempque = collections.deque([])
        while que:
            cs,(cr,cc) = que.popleft()
            if cs>0:
                for dr,dc in move:
                    nr,nc = cr+dr, cc+dc
                    if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0 and board[nr][nc]=='.':
                        board[nr][nc]=str(cnt)
                        if cs-1 == 0:
                            tempque.append((S[cnt-1],(nr,nc)))
                            visited[nr][nc]=1
                        else:
                            que.append((cs-1,(nr,nc)))
                            visited[nr][nc]=1
        ques[cnt-1] = tempque
    # print(ques)                            
    # print(board)
    # print(visitedcnt,visited)
    

tempanswer = [0]*10
for r in range(N):
    for c in range(M):
        if board[r][c] == '#' or board[r][c] == '.':
            continue
        tempanswer[int(board[r][c])]+=1

answer = []
for ta in tempanswer:
    if ta!=0:
        answer.append(ta)
print(*answer)