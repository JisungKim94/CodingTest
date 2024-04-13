import sys
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(10)]

# 걍 빡센구현같은데 아닌가..?

cnt = [5,5,5,5,5]
def check(arr):
    maxN = 0
    asdf = []
    while arr:
        N = 5
        cr,cc = arr.popleft()
        while N>0:
            listt = []
            flag = 1
            for dr in range(N):
                for dc in range(N):
                    nr, nc = cr+dr,cc+dc
                    if 0<=nr<10 and 0<=nc<10:
                        if board[nr][nc] == 0 or visited2[nr][nc]==1:
                            flag = 0
                            break
                        listt.append((nr,nc))
                    else:
                        flag = 0
                        break
                if flag == 0:
                    break
            if flag == 1 and N>=maxN and cnt[N-1]>0:
                asdf = listt
                maxN = N
            N-=1
    
    return maxN,asdf
        
    

import collections
visited2 = [[0]*10 for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def giraffe():
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1 and visited2[i][j] == 0:
                que = collections.deque([(i,j)])
                arr = collections.deque([])
                while que:
                    cr,cc = que.popleft()
                    arr.append((cr,cc))
                    visited[cr][cc] = 1
                    for dr,dc in move:
                        nr,nc = cr+dr,cc+dc
                        if 0<=nr<10 and 0<=nc<10 and board[nr][nc]==1 and visited[nr][nc]==0:
                            visited[nr][nc] = 1
                            que.append((nr,nc))
                n,listt = check(arr)
                print(n,listt)
                if n==0:
                    pass
                else:
                    cnt[n-1]-=1
                    for r,c in listt:
                        visited2[r][c]=1
                
giraffe()
giraffe()

# print(visited)
# print(visited2)
kjs = 1
for i in range(10):
    for j in range(10):
        if visited[i][j] == visited2[i][j] == board[i][j]:
            pass
        else:
            kjs=0
print(cnt)
if kjs:
    answer=0
    for i in cnt:
        answer+=(5-i)
    print(answer)
else:
    print(-1)