import collections
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = [[[] for _ in range(M)] for _ in range(N)]
answer = []
dir = [0,1,2,3] # r,u,l,d
rflct_dir = [1,0,3,2] # u,r,d,l
move = [(0,1),(-1,0),(0,-1),(1,0)]
for i in range(1,2*(N+M)+1):
    if 0<i<=N:
        cdir = 0
        cr,cc = i-1,0
        ans[cr][cc].append((i,2))
    elif N<i<=N+M:
        cdir = 1
        cr,cc = N-1,i-1-N
        ans[cr][cc].append((i,3))
    elif N+M<i<=N+M+N:
        cdir = 2
        cr,cc = N+M+N-i,M-1
        ans[cr][cc].append((i,0))
    else:
        cdir = 3
        cr,cc = 0,N+M+N+M-i
        ans[cr][cc].append((i,1))
    
# print(ans)
for i in range(1,2*(N+M)+1):
    if 0<i<=N:
        cdir = 0
        cr,cc = i-1,0
    elif N<i<=N+M:
        cdir = 1
        cr,cc = N-1,i-1-N
    elif N+M<i<=N+M+N:
        cdir = 2
        cr,cc = N+M+N-i,M-1
    else:
        cdir = 3
        cr,cc = 0,N+M+N+M-i
    
    que = collections.deque([(cdir,(cr,cc))])
    while que:
        # print(i,cdir,(cr,cc))
        cdir,(cr,cc) = que.popleft()
        if board[cr][cc] == 1:
            ndir = rflct_dir[cdir]
        else:
            ndir = cdir
        nr,nc = cr+move[ndir][0], cc+move[ndir][1]
        if 0<=nr<N and 0<=nc<M:
            que.append((ndir,(nr,nc)))
    # print(i,ndir,(cr,cc))
    for a in ans[cr][cc]:
        if ndir == a[1]:
            # print(i,a[0])
            answer.append(a[0])
    # print("")
print(*answer)