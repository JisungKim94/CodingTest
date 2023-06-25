import heapq


def solution(board):
    answer = 0
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    lenrow = len(board)
    lencol = len(board[0])
    for r, v in enumerate(board):
        for c, v2 in enumerate(v):
            if v2 == "R":
                st = (r, c)
            if v2 == "G":
                goal = (r, c)
    # print(st,goal)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        dist = [[float("inf")] * (lencol) for _ in range(lenrow)]
        dist[start[0]][start[1]] = 0
        newcol, newrow = 0, 0
        while q:
            (cost, [noderow, nodecol]) = heapq.heappop(q)
            if cost > dist[noderow][nodecol]:
                continue
            for dx, dy in directions:
                cnt = 0
                while 1:
                    cnt += 1
                    newrow = noderow + dy * cnt
                    newcol = nodecol + dx * cnt
                    if 0 <= newcol < lencol and 0 <= newrow < lenrow:
                        if board[newrow][newcol] == "D":
                            newrow = noderow + dy * (cnt - 1)
                            newcol = nodecol + dx * (cnt - 1)
                            break
                    else:
                        newrow = noderow + dy * (cnt - 1)
                        newcol = nodecol + dx * (cnt - 1)
                        break
                # print(noderow,nodecol,newrow,newcol)
                if 0 <= newcol < lencol and 0 <= newrow < lenrow:
                    if dist[newrow][newcol] > cost + 1:
                        dist[newrow][newcol] = cost + 1
                        heapq.heappush(q, (cost + 1, (newrow, newcol)))
        return dist

    answer = dijkstra(st)
    # print(answer)
    if answer[goal[0]][goal[1]] == float("inf"):
        answer = -1
    else:
        answer = answer[goal[0]][goal[1]]
    return answer
