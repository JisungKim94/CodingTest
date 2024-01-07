r1,c1,r2,c2 = map(int,input().split())
move = [(0,1),(-1,0),(0,-1),(1,0)]
board =[[0]*(abs(c2-c1)+1) for _ in range(abs(r1-r2)+1)]
# print(r1,c1, r2,c2)
# print(r1-r1, c1-c1, r2-r1, c2-c1)
direction = 0
cnt = 1
length = 1
cr,cc = -r1,-c1
dr,dc = move[direction]
# 규칙을 보면 1부터 1칸1칸,2칸,2칸,3칸,3칸 마다 회전한다.
# 그걸 구현하면 댐
max = ((c2-c1+1) * (r2-r1+1))
# 단순히 cnt로 while 조건을 걸면 안되는게..
# in -4444 -4444 -4444 -4444 out 78996545 같은 조건을 못찾음
# 그래서 max를 따로 써줘야 함
while max>0:
    for _ in range(2):
        for _ in range(length):
            if 0<=cr<(abs(r1-r2)+1) and 0<=cc<(abs(c2-c1)+1):
                board[cr][cc] = cnt
                max-=1
                # 이걸 안 걸면 -5 -3 0 0에서 출력 형식이 달라짐
                if max<=0:
                    break
            cr,cc = cr+dr,cc+dc
            cnt+=1
        direction = (direction+1)%4
        dr,dc = move[direction]
    length+=1    

# print(board)

max_len = len(str(cnt))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(board[i][j]).rjust(max_len), end=" ")
    print()
