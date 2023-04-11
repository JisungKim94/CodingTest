# 20:35 ~ 21:24
def isquadtreeable(temparr):
    pre = temparr[0][0]
    for i in range(len(temparr)):
        for j in range(len(temparr)):
            if temparr[i][j] != pre:
                return False
            else:
                pass
            pre = temparr[i][j]
    return True, pre


def kjs(arr, answer):
    n = len(arr) // 2
    temparr = [[0] * n for _ in range(n)]
    row_start, row_stop = 0, n
    col_start, col_stop = 0, n
    for i in range(row_start, row_stop):
        for j in range(col_start, col_stop):
            temparr[i % n][j % n] = arr[i][j]
    if isquadtreeable(temparr) == (True, 0):
        answer[0] = answer[0] - n * n + 1
    elif isquadtreeable(temparr) == (True, 1):
        answer[1] = answer[1] - n * n + 1
    else:
        kjs(temparr, answer)
    row_start, row_stop = n, n + n
    col_start, col_stop = 0, n
    for i in range(row_start, row_stop):
        for j in range(col_start, col_stop):
            temparr[i % n][j % n] = arr[i][j]
    if isquadtreeable(temparr) == (True, 0):
        answer[0] = answer[0] - n * n + 1
    elif isquadtreeable(temparr) == (True, 1):
        answer[1] = answer[1] - n * n + 1
    else:
        kjs(temparr, answer)
    row_start, row_stop = 0, n
    col_start, col_stop = n, n + n
    for i in range(row_start, row_stop):
        for j in range(col_start, col_stop):
            temparr[i % n][j % n] = arr[i][j]
    if isquadtreeable(temparr) == (True, 0):
        answer[0] = answer[0] - n * n + 1
    elif isquadtreeable(temparr) == (True, 1):
        answer[1] = answer[1] - n * n + 1
    else:
        kjs(temparr, answer)
    row_start, row_stop = n, n + n
    col_start, col_stop = n, n + n
    for i in range(row_start, row_stop):
        for j in range(col_start, col_stop):
            temparr[i % n][j % n] = arr[i][j]
    if isquadtreeable(temparr) == (True, 0):
        answer[0] = answer[0] - n * n + 1
    elif isquadtreeable(temparr) == (True, 1):
        answer[1] = answer[1] - n * n + 1
    else:
        kjs(temparr, answer)


def solution(arr):
    answer = [0, 0]
    print(isquadtreeable(arr))
    if isquadtreeable(arr) == (True, 0):
        answer[0] = 1
    elif isquadtreeable(arr) == (True, 1):
        answer[1] = 1
    else:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] == 0:
                    answer[0] = answer[0] + 1
                else:
                    answer[1] = answer[1] + 1
        kjs(arr, answer)
    # print(answer)
    return answer


# print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]) == [4, 9])
# print(
#     solution(
#         [
#             [1, 1, 1, 1, 1, 1, 1, 1],
#             [0, 1, 1, 1, 1, 1, 1, 1],
#             [0, 0, 0, 0, 1, 1, 1, 1],
#             [0, 1, 0, 0, 1, 1, 1, 1],
#             [0, 0, 0, 0, 0, 0, 1, 1],
#             [0, 0, 0, 0, 0, 0, 0, 1],
#             [0, 0, 0, 0, 1, 0, 0, 1],
#             [0, 0, 0, 0, 1, 1, 1, 1],
#         ]
#     )
#     == [10, 15]
# )
temparr = [[0] * 16 for _ in range(16)]
# print(solution(temparr) == [1, 0])
temparr = [[1] * 4 for _ in range(4)]
print(solution(temparr) == [0, 1])
