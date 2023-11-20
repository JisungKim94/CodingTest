import collections
import sys

input = sys.stdin.readline

shape1 = ((0, 0), (0, 1), (0, 2), (0, 3))
shape2 = ((0, 0), (1, 0), (2, 0), (3, 0))

shape3 = ((0, 0), (0, 1), (1, 1), (1, 2))
shape4 = ((0, 1), (1, 0), (1, 1), (2, 0))

shape5 = ((0, 0), (0, 1), (0, 2), (1, 2))
shape6 = ((0, 0), (1, 0), (1, 1), (1, 2))
shape7 = ((0, 0), (0, 1), (1, 0), (2, 0))
shape8 = ((0, 0), (0, 1), (1, 1), (2, 1))

shape9 = ((0, 0), (0, 1), (0, 2), (1, 1))
shape10 = ((1, 0), (1, 1), (1, 2), (0, 1))
shape11 = ((0, 0), (1, 0), (2, 0), (1, 1))
shape12 = ((0, 1), (1, 1), (2, 1), (1, 0))

shape13 = [(0, 0), (0, 1), (1, 0), (1, 1)]
shpaes = [
    shape1,
    shape2,
    shape3,
    shape4,
    shape5,
    shape6,
    shape7,
    shape8,
    shape9,
    shape10,
    shape11,
    shape12,
    shape13,
]


def main():
    t = 1
    while True:
        N = int(input())
        if N == 0:
            break
        board = [list(map(int, input().rstrip().split())) for _ in range(N)]

        move = [(1, 0), (0, 1)]
        answer = -1
        stack = collections.deque([])
        for v in shpaes:
            stack.append(v)

        while stack:
            ca, cb, cc, cd = stack.popleft()
            answer = max(
                answer,
                board[ca[0]][ca[1]]
                + board[cb[0]][cb[1]]
                + board[cc[0]][cc[1]]
                + board[cd[0]][cd[1]],
            )
            for r, c in move:
                na = (ca[0] + r, ca[1] + c)
                nb = (cb[0] + r, cb[1] + c)
                nc = (cc[0] + r, cc[1] + c)
                nd = (cd[0] + r, cd[1] + c)
                if (
                    nd[0] >= N
                    or nc[0] >= N
                    or nb[0] >= N
                    or na[0] >= N
                    or nd[1] >= N
                    or nc[1] >= N
                    or nb[1] >= N
                    or na[1] >= N
                ):
                    pass
                else:
                    stack.append((na, nb, nc, nd))
        print(f"{t}. answer")
        t += 1

    return


if __name__ == "__main__":
    main()
