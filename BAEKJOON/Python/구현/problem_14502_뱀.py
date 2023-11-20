import sys
from collections import deque

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1
L = int(input())
turn = []
for _ in range(L):
    t, d = map(str, input().split())
    turn.append((int(t), d))
turn.sort(reverse=1)


def main():
    d = 0  # 0,1,2,3 : 우 하 좌 상
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상
    snake = deque([(0, 0)])
    cnt = 0
    while 1:
        cr, cc = snake[-1][0], snake[-1][1]
        dr, dc = move[d][0], move[d][1]
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in snake:
            pass
        else:
            break

        if board[nr][nc] == 1:
            board[nr][nc] = 0
            snake.append((nr, nc))
        else:
            snake.popleft()
            snake.append((nr, nc))
        cnt += 1
        if turn:
            if turn[-1][0] == cnt:
                if turn[-1][1] == "D":
                    d += 1
                else:
                    d -= 1
                turn.pop()
        d = d % 4
    print(cnt + 1)


if __name__ == "__main__":
    main()
