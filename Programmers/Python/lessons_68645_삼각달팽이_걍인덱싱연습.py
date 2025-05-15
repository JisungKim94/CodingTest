def left(numb, temp, row, column, n):
    for i in range(row, n):
        temp[i][column] = numb + 1
        numb = numb + 1
    return numb


def bottom(numb, temp, row, column, n):
    for i in range(column, n - 1):
        temp[row - 1][i + 1] = numb + 1
        numb = numb + 1
    return numb


def right(numb, temp, row, column, n):
    for i in range(row - 1, n, -1):
        temp[i][column] = numb + 1
        numb = numb + 1
    return numb


def solution(n):
    temp = [[0] * (i + 1) for i in range(n)]
    num_last = 0
    for i in range(n + 1):
        num_last = num_last + i

    row = 0
    column = 0
    numb = 0
    cnt = 0
    while numb != num_last:
        numb = left(numb, temp, int(cnt), int(cnt / 2), n - int(cnt / 2))
        if numb == num_last:
            break
        # print(temp)
        numb = bottom(numb, temp, n - int(cnt / 2), int(cnt / 2), n - int(cnt))
        if numb == num_last:
            break
        # print(temp)
        numb = right(numb, temp, n - 1 - int(cnt / 2), -1 - int(cnt / 2), int(cnt))
        if numb == num_last:
            break
        # print(temp)
        cnt = cnt + 2

    answer = []
    for i in temp:
        for j in i:
            answer.append(j)
    # print(answer)
    return answer


# print(solution(4) == [1, 2, 9, 3, 10, 8, 4, 5, 6, 7])
# print(solution(5) == [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9])
print(
    solution(6)
    == [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]
)
