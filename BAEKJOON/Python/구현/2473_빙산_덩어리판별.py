import collections

answer = 0
N, M = map(int, input().split())  # 앞의 글자는 n, 뒤의 글자는 m으로 할당됨.
board = [list(map(int, input().split())) for _ in range(N)]

# 덩어리 판별은 어떻게 해야할까???
# 얼음덩이리 개수 구해놓고 dfs나bfs로 탐색해서 그 길이가 덩어리 개수랑 같으면 한 덩어리라고 봤음
# 그런데 녹은 얼음들 처리하다가 좀 헤맸는데.. 
# 1) 시간초과
# for r in range(N):
#     for c in range(M):
#         if board[r][c] == 0:
#             pass
#         else:
#             iceberg.append((r,c))
#
# 2) 내가 생각한대로 안돌아감 for문에 remove나 pop은 걍 절대 하지말자;;
# for r,c in iceberg:
#     if board[r][c] <= 0:
#         iceberg.remove((r,c))
#
# 3) 이게 왜이렇게 생각이 안났는지는 모르겠는데;; 걍 조건걸고 append 하면 되는거였음 귀신에 홀린듯 -_ㅜ
# newiceberg = []
# for r,c in iceberg:
#     if board[r][c] > 0:
#         newiceberg.append((r,c))


iceberg = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            pass
        else:
            iceberg.append((r,c))
move = [(-1,0), (1,0), (0,-1), (0,1)]
while 1:
    # print(board)
    newiceberg = []
    for r,c in iceberg:
        if board[r][c] > 0:
            newiceberg.append((r,c))
    # print(newiceberg)
    visited = [[0]*M for _ in range(N)]
    icesize = len(newiceberg)
    if icesize == 0:
        answer = 0
        break
    visited[newiceberg[0][0]][newiceberg[0][1]] = 1
    flag = 0
    cnt = 0
    
    stack = collections.deque([(newiceberg[0][0],newiceberg[0][1])])
    while stack:
        cr,cc = stack.popleft()
        cnt+=1
        if cnt==icesize or flag:
            flag = 1
        else:
            for dr,dc in move:
                nr,nc = cr+dr, cc+dc
                if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0 and board[nr][nc] > 0:
                    visited[nr][nc]=1
                    stack.append((nr,nc))
    if flag:
        answer+=1
    else:
        break

    meltlist = []
    stack = collections.deque([(newiceberg[0][0],newiceberg[0][1])])
    visited = [[0]*M for _ in range(N)]
    visited[newiceberg[0][0]][newiceberg[0][1]] = 1
    while stack:
        cr,cc = stack.popleft()
        tempmelt = 0
        for dr,dc in move:
            nr,nc = cr+dr, cc+dc
            if 0<=nr<N and 0<=nc<M:
                if board[nr][nc] < 1:
                    tempmelt+=1
                else:
                    if visited[nr][nc]==0:
                        visited[nr][nc]=1
                        stack.append((nr,nc))
        meltlist.append(((cr,cc),tempmelt))
    for (r,c),melt in meltlist:
        board[r][c]-=melt
    iceberg = newiceberg
    

print(answer)