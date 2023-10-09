import heapq
from collections import defaultdict


def solution(n, paths, gates, summits):
    stack = []
    summits.sort()
    summits_set = set(summits)
    dist = [float("inf")] * (n + 1)

    # 내가 직접 만들어서 쓰는 dict보다 아래처럼 deafualt dict 쓰는게 훨배빠름;;; 왜일까? get이 좀 느릴수도 있을듯..!
    # 위에껄론 20번인가 21번 효율성을 맞출수가 없는데 아래껄론 걍통과가 된다.
    # default dict list꼴로 만드는것도 확인!
    # new_paths = {}
    # for path in paths:
    #     new_paths[path[0]] = new_paths.get(path[0],[]) + [(path[1],path[2])]
    #     new_paths[path[1]] = new_paths.get(path[1],[]) + [(path[0],path[2])]
    # print(new_paths)
    new_paths = defaultdict(list)
    # print(new_paths)
    for i, j, w in paths:
        new_paths[i].append((j, w))
        new_paths[j].append((i, w))
    # print(new_paths)
    for gate in gates:
        dist[gate] = 0
        cost, node = 0, gate
        heapq.heappush(stack, (cost, node))
    while stack:
        ccost, cnode = heapq.heappop(stack)
        if cnode in summits_set or ccost > dist[cnode]:
            continue

        for nnode, ncost in new_paths[cnode]:
            ncost = max(ncost, ccost)
            if ncost < dist[nnode]:
                heapq.heappush(stack, (ncost, nnode))
                dist[nnode] = ncost

    min_intensity = [0, float("inf")]
    for summit in summits:
        if dist[summit] < min_intensity[1]:
            min_intensity[0] = summit
            min_intensity[1] = dist[summit]

    return min_intensity


print(
    solution(
        6,
        [
            [1, 2, 3],
            [2, 3, 5],
            [2, 4, 2],
            [2, 5, 4],
            [3, 4, 4],
            [4, 5, 3],
            [4, 6, 1],
            [5, 6, 1],
        ],
        [1, 3],
        [5],
    )
    == [5, 3]
)

# print(
#     solution(
#         7,
#         [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
#         [1],
#         [2, 3, 4],
#     )
#     == [3, 4]
# )

# print(
#     solution(
#         7,
#         [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
#         [3, 7],
#         [1, 5],
#     )
#     == [5, 1]
# )

# print(
#     solution(
#         5,
#         [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],
#         [1, 2],
#         [5],
#     )
#     == [5, 6]
# )
