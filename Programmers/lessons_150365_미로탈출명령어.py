import collections


def solution(n, m, x, y, r, c, k):
    answer = ""
    start_node = [x, y]
    end_node = [r, c]
    curx, cury = x, y
    leftcost = abs(x - r) + abs(y - c)
    if leftcost > k:
        return "impossible"
    way = collections.deque([])
    stack = [(0, (x, y))]
    visited = [[0] * (m + 1) for _ in range(n + 1)]
    visited[x][y] = -1
    directions_dl = [(1, 0), (0, -1)]  # dl x가row y가column임
    directions_all = [(1, 0), (0, -1), (0, 1), (-1, 0)]  # dlru x가row y가column임
    end_node = [n, 1]
    while stack:
        cost, curnode = stack.pop()
        curx, cury = curnode[0], curnode[1]
        leftcost = abs(curx - r) + abs(cury - c)
        if curx == n and cury == 1:
            while leftcost + 2 <= k:
                way.append("r")
                way.append("l")
                k -= 2
            end_node = [r, c]
            directions = directions_all
            flag = 1
        else:
            if k <= leftcost:
                end_node = [r, c]
                directions = directions_all
                flag = 1
            else:
                flag = 0
                directions = directions_dl

        if k > 0:
            for i, j in directions:
                nextx = curx + i
                nexty = cury + j
                nextleftcost = abs(nextx - r) + abs(nexty - c)
                if 0 < nextx < n + 1 and 0 < nexty < m + 1:
                    if flag == 0:
                        visited[nextx][nexty] = cost + 1
                        stack.append((cost + 1, (nextx, nexty)))
                        break
                    elif flag == 1 and nextleftcost < leftcost:
                        visited[nextx][nexty] = cost + 1
                        stack.append((cost + 1, (nextx, nexty)))
                        break

            if i == 1 and j == 0:
                way.append("d")
                k -= 1
            elif i == 0 and j == -1:
                way.append("l")
                k -= 1
            elif i == 0 and j == 1:
                way.append("r")
                k -= 1
            elif i == -1 and j == 0:
                way.append("u")
                k -= 1
    # .....
    # ....E
    # ..S..
    # .....
    # print(stack,way,k,curx,cury,end_node)
    if k % 2 == 1 or k < 0 or end_node != [curx, cury]:
        return "impossible"

    return "".join(way)
