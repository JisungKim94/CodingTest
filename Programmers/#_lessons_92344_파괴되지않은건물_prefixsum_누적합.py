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


# 누적합을 이용한 풀이
# https://nahwasa.com/entry/%EB%88%84%EC%A0%81-%ED%95%A9prefix-sum-2%EC%B0%A8%EC%9B%90-%EB%88%84%EC%A0%81%ED%95%A9prefix-sum-of-matrix-with-java
# 개념은 다음과 같다.
# A = [1,2,3,4,5,6,7]이 있을 때 i부터 j까지 합을 구하고 싶을 때 그냥 단순히 구하면
# A[i] + A[i+1] ... + A[j]가 되고 이는 시간 복잡도 O(N)을 가진다.
# 그 대신 누적합 행렬 하나를 선언하면
# B = [1,3,6,10,15,21,28]이 되고 i,j를 2,4 라 하면
# B[4]-B[2-1] = 15-3 = 12 = A[2]+A[3]+A[4] = 3+4+5 = 12
# B의 시간복잡도은 O(1)
# 2차원 누적합은 좀 더 어렵지만 개념은 같다.
def solution(board, skill):
    answer = 0
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        # 누적합 기록용
        temp[r1][c1] += degree if type == 2 else -degree
        temp[r1][c2 + 1] += -degree if type == 2 else degree
        temp[r2 + 1][c1] += -degree if type == 2 else degree
        temp[r2 + 1][c2 + 1] += degree if type == 2 else -degree
    # skill에 있는 degree 정보들을 한번에 다 넣어둠
    # print(temp)

    # 행 기준 누적합
    for i in range(len(temp) - 1):
        for j in range(len(temp[0]) - 1):
            temp[i][j + 1] += temp[i][j]
    # 열 기준 누적합
    for j in range(len(temp[0]) - 1):
        for i in range(len(temp) - 1):
            temp[i + 1][j] += temp[i][j]
    # print(temp)

    # 기존 배열과 합함
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


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
