# 무뇌식 풀이, 효율성 통과 X
def solution_(board, skill):
    answer = 0
    for type_, r1, c1, r2, c2, degree in skill:
        stream_row = range(r1, r2 + 1)
        stream_col = range(c1, c2 + 1)
        # 여기 아래부분에 2차원 배열을 모든 degree마다 다 참조하므로 시간 복잡도가 O(N*M)
        if type_ == 1:
            for r in stream_row:
                for c in stream_col:
                    board[r][c] = board[r][c] - degree
        else:
            for r in stream_row:
                for c in stream_col:
                    board[r][c] = board[r][c] + degree

    for i in board:
        for j in i:
            if j > 0:
                answer = answer + 1
    return answer


# 누적합 중 구간합을 응용한 풀이 구간합은 1차원 누적합과 달리 2차원 누적합의 응용이다. 즉 응용의 응용
# https://jih3508.tistory.com/50
# 개념은 다음과 같다.
# 행렬의 시작과 끝에 degree를 적어두고(사실은 시작과 끝에 idex error 방지용 +1, 반대쪽 양끝에 -degree) 다음 skill 진행
# skill이 끝나면 그 구간에 같은 값들을 한 번 씩 칠해준다.
def solution(board, skill):
    answer = 0
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        # 누적합 기록용
        temp[r1][c1] += degree if type == 2 else -degree
        temp[r1][c2 + 1] += -degree if type == 2 else degree
        temp[r2 + 1][c1] += -degree if type == 2 else degree
        temp[r2 + 1][c2 + 1] += degree if type == 2 else -degree
        print(temp)
    # skill에 있는 degree 정보들을 한번에 다 넣어둠
    print()
    # print(temp)

    # 행 기준 누적합
    for r in range(len(temp) - 1):
        for c in range(len(temp[0]) - 1):
            temp[r][c + 1] += temp[r][c]
        print(temp)
    print()
    # 열 기준 누적합
    for c in range(len(temp[0]) - 1):
        for r in range(len(temp) - 1):
            temp[r + 1][c] += temp[r][c]
        print(temp)
    print()
    # print(temp)

    # 기존 배열과 합함
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1
    print(board)
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
print(
    solution(
        [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
        [
            [1, 0, 0, 3, 4, 4],
            [1, 2, 0, 2, 3, 2],
            [2, 1, 0, 3, 1, 2],
            [1, 0, 1, 3, 3, 1],
        ],
    )
    == 10
)
# print(
#     solution(
#         [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#         [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]],
#     )
#     == 6
# )
