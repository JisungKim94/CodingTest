import heapq


def solution(n, s, a, b, fares):
    answer = float("inf")
    adj = [[] for _ in range(n + 1)]
    for f, t, c in fares:
        adj[f].append((t, c))
        adj[t].append((f, c))

    def dijkstra(s):
        q = []
        dist = [float("inf")] * (n + 1)
        dist[s] = 0
        heapq.heappush(q, (0, s))
        while q:
            cost, node = heapq.heappop(q)

            if dist[node] < cost:
                continue
            for next_node, c in adj[node]:
                if dist[node] + c < dist[next_node]:
                    dist[next_node] = dist[node] + c
                    heapq.heappush(q, (dist[node] + c, next_node))

        return dist

    kjs = dijkstra(s)
    for i in range(1, n + 1):
        temp = dijkstra(i)
        # print(kjs[i],temp[a],temp[b])
        answer = min(answer, kjs[i] + temp[a] + temp[b])

    return answer
