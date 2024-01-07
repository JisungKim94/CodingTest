import collections
n, m, x, y, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
command = list(map(int, input().split()))

move = [(0,1),(0,-1),(-1,0),(1,0)]
dice = [x,y]

vertical = collections.deque([0,0,0,0])
horizon = collections.deque([0,0,0,0])

for com in command:
    # print(dice,vertical,horizon)
    if com == 1:
        dice[1]+=1
        if 0<=dice[0]<n and 0<=dice[1]<m:
            horizon.appendleft(horizon.pop())
            vertical[1] = horizon[1]
            vertical[3] = horizon[3]
        else:
            dice[1]-=1
            continue
    elif com == 2:
        dice[1]-=1
        if 0<=dice[0]<n and 0<=dice[1]<m:
            horizon.append(horizon.popleft())
            vertical[1] = horizon[1]
            vertical[3] = horizon[3]
        else:
            dice[1]+=1
            continue
    elif com == 3:
        dice[0]-=1
        if 0<=dice[0]<n and 0<=dice[1]<m:
            vertical.append(vertical.popleft())
            horizon[1] = vertical[1]
            horizon[3] = vertical[3]
        else:
            dice[0]+=1
            continue
    else:
        dice[0]+=1
        if 0<=dice[0]<n and 0<=dice[1]<m:
            vertical.appendleft(vertical.pop())
            horizon[1] = vertical[1]
            horizon[3] = vertical[3]
        else:
            dice[0]-=1
            continue
    if board[dice[0]][dice[1]] == 0:
        board[dice[0]][dice[1]] = vertical[3]
    else:
        vertical[3] = board[dice[0]][dice[1]]
        horizon[3] = board[dice[0]][dice[1]]
        board[dice[0]][dice[1]] = 0
    print(vertical[1])
