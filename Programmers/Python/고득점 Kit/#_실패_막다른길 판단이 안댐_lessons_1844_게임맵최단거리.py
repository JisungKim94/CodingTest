def menhatan_dis(x_, y_, m, n):
    return abs(x_ - m) + abs(y_ - n)


def solution(maps):
    answer = 1
    m = len(maps) - 1
    n = len(maps[0]) - 1
    x = 0
    y = 0
    temp = []
    # 위 아래 오른쪽
    checker = [[-1, 0], [+1, 0], [0, +1], [0, -1]]
    been = []
    if (maps[m - 1][n] == 0) & (maps[m][n - 1] == 0) & (maps[m - 1][n - 1] == 0):
        answer = -1
    else:
        while [x, y] != [m, n]:
            # print("x,y =", x, y)
            been.append([x, y])
            for i, j in checker:
                if (x == 0) & (i < 0):
                    pass
                elif (x == m) & (i > 0):
                    pass
                elif (y == n) & (j > 0):
                    pass
                elif (y == 0) & (j < 0):
                    pass
                elif [x + i, y + j] not in been:
                    if maps[x + i][y + j] == 1:
                        temp.append([i, j, menhatan_dis(x + i, y + j, m, n)])
                else:
                    pass
            x = x + min(temp, key=lambda x: x[2])[0]
            y = y + min(temp, key=lambda x: x[2])[1]
            temp = []
            # print("updated x,y =", x, y)
            answer = answer + 1
    print(answer)
    return answer


print(
    solution(
        [
            [1, 0, 1, 1, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 1],
        ]
    )
    == 11
)
print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1],
        ]
    )
    == -1
)
