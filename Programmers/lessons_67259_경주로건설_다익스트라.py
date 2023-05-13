# 3차원 사용해야하는 이유가 좀 생각이 안났었음..
# 방향 고려 안 하면 오답을 추출하는 경우가 있음

import heapq


def solution(board):
    answer = 0
    n = len(board)
    d = [(0, 1, 0), (1, 0, 1), (-1, 0, 2), (0, -1, 3)]

    def dijkstra(sx, sy):
        q = []
        dist = [[[float("inf")] * n for _ in range(n)] for _ in range(4)]
        dirs = 0
        dist[0][0][0] = 0
        dist[1][0][0] = 0
        dist[2][0][0] = 0
        dist[3][0][0] = 0
        heapq.heappush(q, (0, (sx, sy, sx, sy, dirs)))
        while q:
            (c, (x, y, px, py, dirs)) = q.pop()
            if c < dist[dirs][x][y]:
                continue
            for dx, dy, dirs in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    if abs(nx - px) >= 1 and abs(ny - py) >= 1:
                        newcost = c + 600
                    else:
                        newcost = c + 100
                    if newcost < dist[dirs][nx][ny]:
                        dist[dirs][nx][ny] = newcost
                        heapq.heappush(q, (newcost, (nx, ny, x, y, dirs)))
        return dist

    dist = dijkstra(0, 0)
    answer = min(dist[0][-1][-1], dist[1][-1][-1], dist[2][-1][-1], dist[3][-1][-1])
    return answer
