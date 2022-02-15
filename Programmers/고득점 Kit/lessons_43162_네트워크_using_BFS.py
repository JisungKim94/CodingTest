from collections import deque


# BFS 함수 정의
def bfs(n, computers, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:

        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in range(n):
            if not visited[i] and computers[v][i] == 1:
                queue.append(i)
                visited[i] = True


def solution(n, computers):
    answer = 0

    # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            # 정의된 BFS 함수 호출
            bfs(n, computers, i, visited)
            answer += 1

    return answer


# solution(3, [[1, 0, 0], [0, 1, 1], [0, 1, 1]])
# solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
# solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 3
# solution(1, [[1]])  # 1
solution(4, [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1]])  # 1
# solution(
#     5,
#     [
#         [1, 1, 1, 0, 0],
#         [1, 1, 0, 0, 0],
#         [1, 0, 1, 0, 0],
#         [0, 0, 0, 1, 1],
#         [0, 0, 0, 1, 1],
#     ],
# )  # 2
