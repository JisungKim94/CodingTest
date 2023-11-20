#
# Greedy로 풀면 틀리는 문제..
#
# combination으로 갔어야하고 문제 조건이 널널하므로 이거 의심 해봤어야 함
#
from itertools import combinations


def main():
    answer = 10000
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    chicken = []
    house = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                pass
            elif board[r][c] == 1:
                house.append((r + 1, c + 1))
            else:
                chicken.append((r + 1, c + 1))
    min_chickenlength = []

    for (r2, c2) in house:
        minlength = 10000
        for (r1, c1) in chicken:
            minlength = min(minlength, abs(r1 - r2) + abs(c1 - c2))
        min_chickenlength.append(minlength)

    if len(chicken) <= M:
        answer = sum(min_chickenlength)
    else:
        for chicken_ in combinations(chicken, M):
            min_chickenlength = []
            for (r2, c2) in house:
                minlength = 10000
                for (r1, c1) in chicken_:
                    minlength = min(minlength, abs(r1 - r2) + abs(c1 - c2))
                min_chickenlength.append(minlength)
            answer = min(answer, sum(min_chickenlength))
    print(answer)


if __name__ == "__main__":
    main()
