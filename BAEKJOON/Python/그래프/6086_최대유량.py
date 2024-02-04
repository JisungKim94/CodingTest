# 네트워크 흐름이라는 문제 유형이며
# 에드몬드-카프 알고리즘으로 풀 수있다고 함. 더 어려운건 다닉? 디닉? 으로 풀어야한다고 함
# 동일한 유형으로 이분매칭(남여짝 매칭) 문제가 있다고 함..
# 최대유량, 네트워크 플로우, 에드몬드카프, 포드풀커슨
# https://m.blog.naver.com/ndb796/221237111220


import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def bfs(source, pipes, flow):
    queue = deque()
    queue.append(source)

    path = [-1] * 128
    path[source] = source

    while queue:
        u = queue.popleft()
        for v in range(65, 123):
            if path[v] == -1 and pipes[u][v] - flow[u][v] > 0: # v노드를 방문한 적 없고, pipes[u][v]가 흐를 수 있음
                # 큐에 추가
                queue.append(v)
                # 경로를 저장
                path[v] = u
    return path

def edmonds_karp(pipes):
    source, sink = 65, 90
    flow = [[0]*128 for _ in range(128)]
    result = 0

    while True:
        path = bfs(source, pipes, flow)
        # sink까지 못 갔으면(경로에 sink가 없으면) break
        if path[sink] == -1:
            return result

        min_value = float('inf')

        idx = sink
        # 최소 유량(경로상에 있는 간선의 용량 중 가장 작은 것)을 거꾸로 탐색
        while idx != source:
            min_value = min(min_value, pipes[path[idx]][idx] - flow[path[idx]][idx])
            idx = path[idx]
        # flow, 유령간선에 거꾸로 탐색하면서 최소유량만큼 더하기, 빼기
        idx = sink
        while idx != source:
            flow[path[idx]][idx] += min_value
            flow[idx][path[idx]] -= min_value
            idx = path[idx]

        result += min_value

def solution():
    n = int(input())
    # pipes[u][v] = 파이프 면적(흐를 수 있는 최대값)
    pipes = [[0]*128 for _ in range(128)]
    for _ in range(n):
        u, v, x = input().split()
        u = ord(u)
        v = ord(v)
        x = int(x)
        pipes[u][v] += x
        pipes[v][u] += x
    print(edmonds_karp(pipes))

solution()