import heapq


def solution(r, c, board):
    answer = []

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    stack = []

    dist = [[float("inf")] * len(board[0]) for _ in range(len(board))]

    r, c = r - 1, c - 1

    dist[r][c] = 0

    # print(dist)

    heapq.heappush(stack, (0, r, c))

    while stack:
        cost, nr, nc = heapq.heappop(stack)

        if cost > dist[nr][nc]:
            continue

        for dc, dr in direction:
            if 0 <= nc + dc < len(board[0]) and 0 <= nr + dr < len(board):
                next_node = (nr + dr, nc + dc)

            if board[nr][nc] == board[next_node[0]][next_node[1]]:
                next_cost = cost

            else:
                next_cost = cost + 1

            if next_cost < dist[next_node[0]][next_node[1]]:
                dist[next_node[0]][next_node[1]] = next_cost

                heapq.heappush(stack, (next_cost, next_node[0], next_node[1]))

    # print(dist)

    dp = [0] * 1001

    for r in range(len(dist)):
        for c in range(len(dist[0])):
            dp[dist[r][c]] += 1

    maxlvcnt = max(dp)

    for i, v in enumerate(dp):
        if v == maxlvcnt:
            maxlv = i

    # print(maxlv)

    for r in range(len(dist)):
        for c in range(len(dist[0])):
            if dist[r][c] == maxlv:
                answer.append([r + 1, c + 1])

    # print(answer)

    return answer


print(
    solution(
        3,
        2,
        [
            [5, 4, 3, 4, 4, 4],
            [1, 3, 2, 3, 3, 5],
            [2, 3, 4, 5, 5, 1],
            [2, 2, 3, 4, 4, 3],
        ],
    )
    == [[1, 4], [1, 5], [1, 6], [2, 6], [3, 6], [4, 4], [4, 5]]
)

print(
    solution(
        3,
        3,
        [
            [7, 9, 7, 9, 7],
            [9, 7, 9, 7, 9],
            [7, 9, 7, 9, 7],
            [9, 7, 9, 7, 9],
            [7, 9, 7, 9, 7],
        ],
    )
    == [[1, 2], [1, 4], [2, 1], [2, 5], [4, 1], [4, 5], [5, 2], [5, 4]]
)
