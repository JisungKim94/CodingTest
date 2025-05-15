import collections


# 전체 탐색 하니까 당연히 시간초과 나지 임마..
# 그리고 a,b,c == y일때 리턴한게 최소가 아닐수도 있음 잘못된 풀이임
# def solution(x, y, n):
#     answer = 0
#     tree = collections.deque(
#         [
#             collections.deque([(x)]),
#             collections.deque([(x + n, x * 2, x * 3)]),
#         ]
#     )
#     depth = 2
#     cur = 1000001
#     if x + n == y or x * 2 == y or x * 3 == y:
#         # print(1)
#         return 1
#     while 1:
#         temp = collections.deque()
#         for i in range(len(tree[depth - 1])):
#             for j in range(3):
#                 a = tree[depth - 1][i][j] + n
#                 b = tree[depth - 1][i][j] * 2
#                 c = tree[depth - 1][i][j] * 3
#                 if a == y or b == y or c == y:
#                     # print(depth)
#                     return depth
#                 temp.append((a, b, c))
#                 cur = min(a, b, c, cur)
#         if cur > y:
#             break
#         tree.append(temp)
#         depth = depth + 1
#     return -1


# dist 으로 해당 숫자까지 걸리는 계산 수를 나타냄
# dist는 0일때만 이전까지 걸린 수에 +1을 해주는데
# 그래도 되는 이유는 que에 순서대로 박히기 때문에
# 0이 아닐 때 온 애는 항상 같거나 더 큰 계산 수를 가지기 때문
def solution(x, y, n):
    def bfs(x, y, n):
        q = collections.deque()
        dist[x] = 1
        q.append(x)

        while q:
            x = q.popleft()
            if 0 <= x + n <= 1000000 and dist[x + n] == 0:
                dist[x + n] = dist[x] + 1
                q.append(x + n)
            if 0 <= x * 2 <= 1000000 and dist[x * 2] == 0:
                dist[x * 2] = dist[x] + 1
                q.append(x * 2)
            if 0 <= x * 3 <= 1000000 and dist[x * 3] == 0:
                dist[x * 3] = dist[x] + 1
                q.append(x * 3)

    dist = [0] * 1000001
    bfs(x, y, n)

    return dist[y] - 1


#         []
#   []    []    []
# [][][][][][][][][]

print(solution(10, 40, 5) == 2)
print(solution(10, 40, 30) == 1)
print(solution(2, 5, 4) == -1)
print(solution(2, 199999, 3) == -1)
