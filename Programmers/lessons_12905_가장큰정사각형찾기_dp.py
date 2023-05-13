def solution(board):
    answer = 0
    dp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    # print(dp)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
            answer = max(answer, dp[i + 1][j + 1])
    # print(dp)
    # print(answer)
    return answer**2
