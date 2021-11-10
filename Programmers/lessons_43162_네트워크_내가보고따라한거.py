def to_last_node(node, visited, computers):
    visited[node] = 1
    relation = computers[node]

    for idx_, is_connected in enumerate(relation):
        if visited[idx_] == 0:
            if is_connected == True:
                to_last_node(idx_, visited, computers)


def solution(n, computers):
    visited = [0] * n
    answer = 0
    while 0 in visited:
        for i in range(n):
            if visited[i] == 0:
                to_last_node(i, visited, computers)
                answer += 1
    print(answer)
    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
