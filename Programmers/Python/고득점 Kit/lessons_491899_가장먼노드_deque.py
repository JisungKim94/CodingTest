import collections


def solution(n, vertex):
    answer = 0
    # 각 노드와 연결된 노드표시
    # 아.. 이렇게 하는거구나
    graph = [[] * n for i in range(n + 1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # [node, visted] 다녀갔으면 1
    queue = collections.deque([1])
    visited = [0] * (n + 1)
    visited[1] = 1
    # print(visited)
    print(graph)

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            # 1번 노드에서 확인 해 볼 애들은 1번과 연결되어(graph에 있는)있는 3,2
            # 3번 노드에서 확인해 볼 애들은 연결되어(graph에 있는)있는 6,4,2,1 중 6,4
            # 왜냐? 1에서 왔으니까 1은 빼고 최단거리니까 1에서 가볼 수 있었던 2도 빼야댐 즉 6,4만 확인
            # if visited[i] == 0: 에서 이 알고리즘이 적용
            # visited[i] = visited[node] + 1 에선 전 노드까지 걸린 길이를 누적 해 주는부분임 총 거리를 나타냄
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[node] + 1
    print(visited)
    # visited 중에 count(this)가 몇개 있는지
    # 즉, 총 몇 개의 node를 거쳐서 도달하는지 세는거 3이면 1을 포함해서 총 3개
    answer = visited.count(max(visited))
    print(answer)
    return answer


# 위에는 당시에 풀었던 풀이고
# 아래는 다익스트라를 이용한 내 풀이
# 이거 풀 때
#         for next_node in graph[node]:
#            if cost+1<dist[next_node]:
# 이거를
#         for next_node in graph[node]:
#            if cost<dist[next_node]:
# 이걸로 해서 틀렸었음;;;
import heapq
import collections


def dijstra(graph, n):
    heap = []
    dist = [float("inf")] * (n + 1)
    dist[0] = 0
    dist[1] = 0
    heapq.heappush(heap, (0, 1))

    while heap:
        cost, node = heapq.heappop(heap)

        if dist[node] < cost:
            continue

        for next_node in graph[node]:
            if cost + 1 < dist[next_node]:
                dist[next_node] = cost + 1
                heapq.heappush(heap, (cost + 1, next_node))

    return dist


def solution(n, vertex):
    answer = 0
    graph = collections.defaultdict(list)
    for v0, v1 in vertex:
        graph[v0].append(v1)
        graph[v1].append(v0)

    tmp = dijstra(graph, n)
    answer = tmp.count(max(tmp))

    return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
