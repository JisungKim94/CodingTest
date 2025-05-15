def solution(m, n, board):
    answer = 0
    temp = []
    board_ = [[""] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            board_[i][j] = board[i][j]

    while 1:
        for i in range(m):
            for j in range(n):
                if i == m - 1 or j == n - 1:
                    pass
                else:
                    if (
                        board_[i][j] == board_[i][j + 1]
                        and board_[i][j] == board_[i + 1][j]
                        and board_[i][j] == board_[i + 1][j + 1]
                    ):
                        # print(i, j)
                        if board_[i][j] != "-":
                            temp.append((i, j))

        if len(temp) == 0:
            break

        for i, j in temp:
            board_[i][j] = "-"
            board_[i][j + 1] = "-"
            board_[i + 1][j] = "-"
            board_[i + 1][j + 1] = "-"
        temp = []

        i_ = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m or j == n:
                    pass
                else:
                    if board_[i][j] == "-":
                        i_ = i
                        while board_[i][j] == "-":
                            i_ = i_ - 1
                            if i_ < 0:
                                break
                            if board_[i_][j] != "-":
                                board_[i][j] = board_[i_][j]
                                board_[i_][j] = "-"

    for i in range(m):
        for j in range(n):
            if board_[i][j] == "-":
                answer = answer + 1
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]) == 14)
print(
    solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) == 15
)
