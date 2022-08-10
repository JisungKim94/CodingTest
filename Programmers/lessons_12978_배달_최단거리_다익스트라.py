import heapq


def dijkstra(dist, adj):
    # 출발노드를 기준으로 각 노드들의 최소비용 탐색
    heap = []
    heapq.heappush(heap, [0, 1])  # 거리,노드
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(heap, [cost + c, n])


def solution(N, road, K):

    # 총 5개지만, 0,1,2,3,4,5 로 만들고 0 안쓰는 방식으로 짤거라서 길이는 6으로 만들자

    dist = [float("inf")] * (N + 1)  # dist 배열 만들고 최소거리 갱신할거임
    dist[1] = 0  # 1번은 자기자신이니까 거리 0
    adj = [[] for _ in range(N + 1)]  # 거리&노드 기록할 배열
    for r in road:
        # 양방향 통행이 가능하므로 두쪽 다 넣어줌
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])

    # 이제 위 준비과정이 끝났으니 다익스트라 구현
    # https://blog.naver.com/PostView.naver?blogId=ndb796&logNo=221234424646&redirect=Dlog&widgetTypeCall=true&directAccess=false
    dijkstra(dist, adj)

    return len([i for i in dist if i <= K])


print(
    solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
    == 4
)
print(
    solution(
        6,
        [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]],
        4,
    )
    == 4
)
