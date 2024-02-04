import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())

# 능지문제였는데 오래걸림 능지가 딸려가...
# 그리고 맞춰도 제대로 맞춘게 아닌게 나랑 비슷한 풀이인데 난 2를 실제로 다 돌려버렸는데
# 아래처럼 2x2칸만 만들어놓고 %해서 봐도 결과는 같음 끝까지 가 보면 결국 다 돌려도 저기 4칸안에 들어오니까..
# import sys

# input = sys.stdin.readline
# n,m,k = map(int,input().split())
# clean = [[False] * 2 for _ in range(2)]
# for  _ in range(k):
#   x, y = map(int,input().split())
#   clean[x%2][y%2] = True

# if clean[0][0] and clean[0][1] and clean[1][0] and clean[1][1]:
#   print("YES")
# else:
#   print("NO")


board = [[0]*M for _ in range(N)]
pang2 = []
for _ in range(K):
    r,c = map(int, input().split())
    pang2.append((r-1,c-1))
for r,c in pang2:
    cr,cc = r,c
    if board[cr][cc] == 1:
        continue
    board[cr][cc] = 1
    while 0<=cr<N:
        cc = c
        while 1:
            if 0<=cc<M:
                board[cr][cc] = 1
            else:
                break
            cc = cc+2
        cr=cr+2
    cr,cc = r,c
    while 0<=cr<N:
        cc = c
        while 1:
            if 0<=cc<M:
                board[cr][cc] = 1
            else:
                break
            cc = cc-2
        cr=cr+2
    cr,cc = r,c
    while 0<=cr<N:
        cc = c
        while 1:
            if 0<=cc<M:
                board[cr][cc] = 1
            else:
                break
            cc = cc+2
        cr=cr-2
    cr,cc = r,c
    while 0<=cr<N:
        cc = c
        while 1:
            if 0<=cc<M:
                board[cr][cc] = 1
            else:
                break
            cc = cc-2
        cr=cr-2
# print(board)
if board[0][0] and board[1][0] and board[0][1] and board[1][1]:
    print("YES")
else: 
    print("NO")