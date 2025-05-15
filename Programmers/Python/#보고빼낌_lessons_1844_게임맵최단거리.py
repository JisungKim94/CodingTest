from collections import deque

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def solution(maps):
    m = len(maps)
    n = len(maps[0])
    visited = [[-1 for _ in range(n)] for _ in range(m)]
    que = deque()
    que.append([0, 0])
    visited[0][0] = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            temp_x = x + d[i][0]
            temp_y = y + d[i][1]
            # 막다른 길로 가거나, 지나온 길로 탐색하지 않도록
            if -1 < temp_x < m and -1 < temp_y < n:
                # 길이 있는지 확인
                if maps[temp_x][temp_y] == 1:
                    # 안가본 길이라면
                    if visited[temp_x][temp_y] == -1:
                        # 이전 위치에서 +1
                        visited[temp_x][temp_y] = visited[x][y] + 1
                        que.append([temp_x, temp_y])

    answer = visited[-1][-1]
    return answer


print(
    solution(
        [
            [1, 0, 1, 1, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 1],
        ]
    )
    == 12
)
# print(
#     solution(
#         [
#             [1, 0, 1, 1, 1],
#             [1, 0, 1, 0, 1],
#             [1, 0, 1, 1, 1],
#             [1, 1, 1, 0, 1],
#             [0, 0, 0, 0, 1],
#         ]
#     )
#     == 11
# )
# print(
#     solution(
#         [
#             [1, 0, 1, 1, 1],
#             [1, 0, 1, 0, 1],
#             [1, 0, 1, 1, 1],
#             [1, 1, 1, 0, 0],
#             [0, 0, 0, 0, 1],
#         ]
#     )
#     == -1
# )
