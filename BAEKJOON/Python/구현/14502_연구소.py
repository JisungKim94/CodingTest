import itertools
import collections
import copy


def main():
    answer = 0
    N, M = map(int, input().split())  # 앞의 글자는 n, 뒤의 글자는 m으로 할당됨.
    board = [list(map(int, input().split())) for _ in range(N)]

    virus = []
    place = []
    wall = []
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0:
                place.append((r, c))
            elif board[r][c] == 1:
                wall.append((r, c))
            else:
                virus.append((r, c))
    comb = list(itertools.combinations(place, 3))
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(len(comb)):
        stack = collections.deque(virus)
        contaminated = copy.deepcopy(virus)
        while stack:
            cr, cc = stack.popleft()

            for r, c in move:
                nr, nc = cr + r, cc + c
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 1:
                    pass
                else:
                    continue
                if (nr, nc) not in contaminated and (nr, nc) not in comb[i]:
                    contaminated.append((nr, nc))
                    stack.append((nr, nc))
        answer = max(answer, N * M - len(contaminated) - len(wall) - 3)
    print(answer)


if __name__ == "__main__":
    main()
