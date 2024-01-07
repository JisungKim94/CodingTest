import collections
N = int(input())
board = [list(map(str, input().rstrip().split())) for _ in range(N)]
# print(board)
def calc(ncost):
    if "+"==ncost[1]:
        num1,oper,num2 = int(ncost[0]),ncost[1],int(ncost[2])
        return [num1 + num2]
    elif "-"==ncost[1]:
        num1,oper,num2 = int(ncost[0]),ncost[1],int(ncost[2])
        return [num1 - num2]
    elif "*"==ncost[1]:
        num1,oper,num2 = int(ncost[0]),ncost[1],int(ncost[2])
        return [num1 * num2]
    else:
        pass

stack = collections.deque([([board[0][0]],(0,0))])
move = [(1, 0), (0, 1)]
minanswer,maxanswer = 5**6,-5**6
while stack:
    ccost,(cr,cc) = stack.popleft()
    if cr==N-1 and cc==N-1:
        # print(ccost)
        minanswer = min(int(ccost[0]),minanswer)
        maxanswer = max(int(ccost[0]),maxanswer)
        continue        
    for dr,dc in move:
        nr,nc = cr+dr, cc+dc
        if 0<=nr<N and 0<=nc<N:
            ccost.append(board[nr][nc])
            ncost = ccost
            if len(ncost) == 3:
                ncost = calc(ncost)
            else:
                pass
            stack.append((ncost[:],(nr,nc)))
            ccost.pop()
print(maxanswer, minanswer)