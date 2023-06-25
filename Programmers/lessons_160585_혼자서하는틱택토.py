def numofOX(board):
    numO, numX = 0, 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == "O":
                numO += 1
            elif board[r][c] == "X":
                numX += 1
            else:
                pass
    return numO, numX


def who_madeit(board):
    Omade, Xmade = 0, 0
    for r in range(3):
        tmp = []
        for c in range(3):
            if board[r][c] == "O":
                tmp.append("O")
            if board[r][c] == "X":
                tmp.append("X")
        if tmp == ["O", "O", "O"]:
            Omade = 1
        if tmp == ["X", "X", "X"]:
            Xmade = 1

    for r in range(3):
        tmp = []
        for c in range(3):
            if board[c][r] == "O":
                tmp.append("O")
            if board[c][r] == "X":
                tmp.append("X")
        if tmp == ["O", "O", "O"]:
            Omade = 1
        if tmp == ["X", "X", "X"]:
            Xmade = 1

    tmp = [board[0][0], board[1][1], board[2][2]]
    if tmp == ["O", "O", "O"]:
        Omade = 1
    if tmp == ["X", "X", "X"]:
        Xmade = 1
    tmp = [board[0][2], board[1][1], board[2][0]]
    if tmp == ["O", "O", "O"]:
        Omade = 1
    if tmp == ["X", "X", "X"]:
        Xmade = 1

    return Omade, Xmade


def solution(board):
    answer = 1
    numO, numX = numofOX(board)
    Omade, Xmade = who_madeit(board)

    if Omade == 1 and Xmade == 1:
        answer = 0
    if Omade == 1 and (numX + 1) != numO:
        answer = 0
    if Xmade == 1 and numX != numO:
        answer = 0
    if (numO - numX) == 0 or (numO - numX) == 1:
        pass
    else:
        answer = 0

    return answer
