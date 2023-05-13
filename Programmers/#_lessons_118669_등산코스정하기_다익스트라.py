from collections import defaultdict
from heapq import heappop, heappush

# https://techblog-history-younghunjo1.tistory.com/248
def dijkstra(n, adj, gates, summits_set):
    # 2) heap 만들기
    pq = []  # (cost, 현재 위치)
    # 3) 현재 거리정보 만들기
    dist = [float("inf")] * (n + 1)

    # 모든 출발지를 우선순위 큐에 삽입
    for gate in gates:
        heappush(pq, (0, gate))
        dist[gate] = 0

    # 산봉우리에 도착할 때까지 반복
    # 4) 힙이 blank 일 때 까지 반복
    while pq:
        cost, node = heappop(pq)

        # 산봉우리이거나 더 긴 거리가 소요되면 더 이상 이동하지 않음
        if node in summits_set or cost > dist[node]:
            continue

        # 이번 위치에서 이동할 수 있는 곳으로 이동
        # 5) 현재 확인중인 node의 graph 정보를 받아서
        for weight, next_node in adj[node]:
            # next_node 위치에 더 작은 intensity로 도착할 수 있다면 큐에 넣지 않음
            # (출입구는 이미 0으로 세팅되어있기 때문에 방문하지 않음)
            # 6) heap(지금까지 저장했던 값) 과 adj(그래프 정보)를 비교해서
            # 업데이트를 해야하는 상황이면 dist(거리정보)를 업데이트하고
            # 7) 얘는 다시 확인을 해 봐야 하니까 heap에 또 넣어줌
            new_intensity = max(cost, weight)
            if new_intensity < dist[next_node]:
                dist[next_node] = new_intensity
                heappush(pq, (new_intensity, next_node))

    return dist


# n: 노드 수
# gates: 출입구, sumits: 산봉우리
def solution(n, paths, gates, summits):

    summits.sort()
    summits_set = set(summits)
    # adj : 등산로 정보 (graph)
    # 1) graph 정보 입력하기
    adj = defaultdict(list)
    for i, j, w in paths:
        adj[i].append((w, j))
        adj[j].append((w, i))

    dist = dijkstra(n, adj, gates, summits_set)

    # 구한 cost 중 가장 작은 값 반환
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
