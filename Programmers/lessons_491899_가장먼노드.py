import collections

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


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
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[node] + 1
    print(visited)
    # visited 중에 count(this)가 몇개 있는지
    # 즉, 총 몇 개의 node를 거쳐서 도달하는지 세는거 3이면 1을 포함해서 총 3개
    answer = visited.count(max(visited))
    print(answer)
    return answer


solution(n, vertex)
