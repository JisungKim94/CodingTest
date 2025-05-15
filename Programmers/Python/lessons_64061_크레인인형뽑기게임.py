from collections import deque


def solution(board, moves):
    answer = 0
    cnt = 0
    que = deque([-1])

    for val in moves:
        for i in range(0, len(board)):
            cnt = cnt + 1
            if cnt >= len(board):
                cnt = 0
            if board[cnt - 1][val - 1] != 0:
                if que[-1] == board[cnt - 1][val - 1]:
                    que.pop()
                    answer = answer + 2
                else:
                    que.append(board[cnt - 1][val - 1])

                board[cnt - 1][val - 1] = 0
                # print(que)
                # print(val, cnt)
                cnt = 0
                break
    que.popleft()
    # print(answer)
    # print(que)

    return answer


print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
    )
    == 4
)
