def solution(board, skill):
    answer = 0
    prefixsumboard = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for type_, r1, c1, r2, c2, damage in skill:
        if type_ == 1:
            prefixsumboard[r1][c1] += -damage
            prefixsumboard[r1][c2 + 1] += damage
            prefixsumboard[r2 + 1][c1] += damage
            prefixsumboard[r2 + 1][c2 + 1] += -damage
        else:
            prefixsumboard[r1][c1] += damage
            prefixsumboard[r1][c2 + 1] += -damage
            prefixsumboard[r2 + 1][c1] += -damage
            prefixsumboard[r2 + 1][c2 + 1] += damage
    # print(prefixsumboard)

    prer = -1
    for r in range(len(prefixsumboard)):
        for c in range(len(prefixsumboard[0])):
            if prer == -1:
                pass
            else:
                prefixsumboard[r][c] = prefixsumboard[prer][c] + prefixsumboard[r][c]
        prer = r
    # print(prefixsumboard)

    for r in range(len(prefixsumboard)):
        prec = -1
        for c in range(len(prefixsumboard[0])):
            if prec == -1:
                pass
            else:
                prefixsumboard[r][c] = prefixsumboard[r][prec] + prefixsumboard[r][c]
            prec = c
    # print(prefixsumboard)

    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] = board[r][c] + prefixsumboard[r][c]
            if board[r][c] > 0:
                answer += 1
    # print(board)
    # print(answer)

    return answer


# print(
#     solution(
#         [
#             [5, 5, 5, 5, 5],
#             [5, 5, 5, 5, 5],
#             [5, 5, 5, 5, 5],
#             [5, 5, 5, 5, 5],
#             [5, 5, 5, 5, 5],
#         ],
#         [
#             [1, 0, 0, 4, 4, 2],
#             [1, 1, 1, 3, 3, 1],
#         ],
#     )
#     == 25
# )
# print(
#     solution(
#         [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
#         [
#             [1, 0, 0, 3, 4, 4],
#             [1, 2, 0, 2, 3, 2],
#             [2, 1, 0, 3, 1, 2],
#             [1, 0, 1, 3, 3, 1],
#         ],
#     )
#     == 10
# )
print(
    solution(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]],
    )
    == 6
)
# print(
#     solution(
#         [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#         [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]],
#     )
#     == 6
# )
