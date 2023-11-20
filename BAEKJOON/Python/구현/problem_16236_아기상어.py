import sys
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# bfs를 돌릴 때 가장위, 가장 왼쪽을 최고 순위로 놓고싶어서
# move = [(-1, 0), (0, -1), (0, 1), (1, 0)] 이렇게 했는데
# 이렇게 하면 거리가 2일때 아래와 같은 순서로 찾는다.
#        5
#     6  1  7
#  8  2  0  3  12
#     9  4  10
#        11
# 12번이 9번보다 느리므로 내가 원하는 결과가 안나옴..
# 그래서 그냥 가까운 거리를 다 찾고 소팅을 해줬다.


def main():
    answer = 0
    fish = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == 9:
                shark = [2, 0, 0, (r, c)]
                board[r][c] = 0
                startr, startc = r, c
                break
    move = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    stack = deque([shark])
    while stack:
        visited = []
        tempsharks = []
        while stack:
            s_csize, nyam, ccost, (s_cr, s_cc) = stack.popleft()
            if board[s_cr][s_cc] != 0 and board[s_cr][s_cc] < s_csize:

                shark = [s_csize, nyam, ccost, (s_cr, s_cc)]
                tempsharks.append(shark)
                # print(shark, answer)
            for dr, dc in move:
                s_nr, s_nc = s_cr + dr, s_cc + dc
                if (
                    0 <= s_nr < N
                    and 0 <= s_nc < N
                    and board[s_nr][s_nc] <= s_csize
                    and (s_nr, s_nc) not in visited
                ):
                    stack.append((s_csize, nyam, ccost + 1, (s_nr, s_nc)))
                    visited.append((s_nr, s_nc))
        tempsharks.sort(key=lambda x: (-x[2], -x[3][0], -x[3][1]))
        # print(tempsharks)
        if tempsharks:
            # tempsharks = s_csize, nyam, ccost, (s_cr, s_cc)
            # 각각 상어 크기, 상어가 먹은 물고기, 이동거리, 좌표
            startr, startc = tempsharks[-1][3][0], tempsharks[-1][3][1]
            board[startr][startc] = 0
            answer += tempsharks[-1][2]
            tempsharks[-1][1] += 1
            if tempsharks[-1][1] == tempsharks[-1][0]:
                tempsharks[-1][0] += 1
                tempsharks[-1][1] = 0
            tempsharks[-1][2] = 0

            stack = deque([tempsharks[-1]])

    print(answer)


if __name__ == "__main__":
    main()
