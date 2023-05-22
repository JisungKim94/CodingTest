import heapq


def solution(maps):
    answer = 0
    for y, rv in enumerate(maps):
        for x, cv in enumerate(rv):
            if cv == "S":
                start = (x, y)
            elif cv == "L":
                lever = (x, y)
            elif cv == "E":
                exit = (x, y)
    # print(start,lever)

    def dijkstra(start, cost):
        q = []
        leny, lenx = len(maps), len(maps[0])
        dist = [[float("inf")] * (lenx + 1) for _ in range(leny + 1)]
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heapq.heappush(q, (cost, start))
        dist[start[1]][start[0]] = cost

        while q:
            cost, (x, y) = heapq.heappop(q)
            if cost < dist[y][x]:
                continue
            for dx, dy in d:
                nextx, nexty = x + dx, y + dy
                if 0 <= nextx < lenx and 0 <= nexty < leny:
                    newcost = cost + 1
                    if newcost < dist[nexty][nextx] and maps[nexty][nextx] != "X":
                        dist[nexty][nextx] = newcost
                        heapq.heappush(q, (newcost, (nextx, nexty)))
        return dist

    temp = dijkstra(start, 0)
    # print(temp)
    newstart = temp[lever[1]][lever[0]]
    temp = dijkstra(lever, newstart)
    # print(temp)

    if temp[exit[1]][exit[0]] != float("inf"):
        answer = temp[exit[1]][exit[0]]
    else:
        answer = -1

    return answer


# print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]) == 16)
print(solution(["SOOOLO", "OOOOOO", "OXXXXO", "OOOOOE"]) == 8)
# print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]) == -1)
