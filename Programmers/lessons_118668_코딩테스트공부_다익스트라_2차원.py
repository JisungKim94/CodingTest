import heapq


def solution(alp, cop, problems):
    answer = 0

    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    problems.sort(key=lambda x: (x[0], x[1]))
    # print(problems)
    max_alp = max(problems, key=lambda x: x[0])[0]
    max_cop = max(problems, key=lambda x: x[1])[1]
    # print(max_alp,max_cop)
    dist = [[float("inf")] * (max_cop + 1) for _ in range(max_alp + 1)]

    # WTF
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    def dijkstra(init_alp, init_cop):
        dist[init_alp][init_cop] = 0
        q = [(0, (init_alp, init_cop))]
        heapq.heapify(q)

        while q:
            c, (n_alp, n_cop) = heapq.heappop(q)
            # que에 담겨져 있을 때 dist가 최소를 찾아버릴 경우 무시
            if dist[n_alp][n_cop] < c:
                continue
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                next_alp = min(n_alp + alp_rwd, max_alp)
                next_cop = min(n_cop + cop_rwd, max_cop)
                # probelms 중에서 인접노드로 쓸 수 있는(풀 수 있는)
                if alp_req <= n_alp and cop_req <= n_cop:
                    # 여까지 온 cost + 다음 cost
                    temp_cost = dist[n_alp][n_cop] + cost
                    # cost는 항상 1보단 크니까 <=가 아니고 <
                    if temp_cost < dist[next_alp][next_cop]:
                        # print(temp_cost,next_alp,next_cop)
                        dist[next_alp][next_cop] = temp_cost
                        heapq.heappush(q, (temp_cost, (next_alp, next_cop)))

    try:
        dijkstra(alp, cop)
    except:
        IndexError()
        print("IE")
    # print(dist[max_alp][max_cop])
    answer = dist[max_alp][max_cop]
    return answer
