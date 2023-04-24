""" 
union-find : https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html / https://brenden.tistory.com/33
Kruskal : https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html
MST
"""


class union:
    def __init__(self, n):
        self.root = list(range(n))
        self.size = n

    def find(self, index):
        if index == self.root[index]:
            return index
        else:
            self.root[index] = self.find(self.root[index])
            return self.root[index]

    # def find(self, index):
    # find 재귀 꼴을 안쓰고 푸는법
    # return self.root[index]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            # 사실상 여기 오면 cycle 형성이라는 말이라서
            # continue에 의해 여기 걸리진 않는다.
            return
        else:
            self.root[y] = x

        # find 재귀 꼴을 안쓰고 푸는법
        # for i in range(self.size):
        #     if self.find(i) == y:
        #         self.root[i] = x

    @property
    def length(self):
        return len(set(self.data))


def solution(n, costs):
    answer = 0
    disjointset = union(n)
    # route = []
    # 간선들의 가중치 오름차순 정렬
    costs = sorted(costs, key=lambda x: x[2])

    for cost in costs:
        if disjointset.find(cost[0]) == disjointset.find(cost[1]):
            # cycle이 형성되면 그 node를 route에 추가하지 않는다.
            # 예를들어 cost[0]의 꼭대기에 0이 있는데
            # cose[1]의 꼭대기에도 0이 있다면 얘내 둘이 연결되면 cycle이 생김
            continue
        disjointset.union(cost[0], cost[1])
        # route.append((cost[0], cost[1]))
        answer += cost[2]

    # print(disjointset.root)
    # print(route)
    # print(answer)
    return answer


# class 없는 답
def solution(n, costs):
    answer = 0
    root = list(range(n))
    # route = []
    # 간선들의 가중치 오름차순 정렬
    costs = sorted(costs, key=lambda x: x[2])

    def union(x, y, root):
        x, y = find(x, root), find(y, root)
        root[y] = x

    def find(index, root):
        if index == root[index]:
            return index
        else:
            root[index] = find(root[index], root)
            return root[index]

    for cost in costs:
        if find(cost[0], root) == find(cost[1], root):
            # cycle이 형성되면 그 node를 route에 추가하지 않는다.
            # 예를들어 cost[0]의 꼭대기에 0이 있는데
            # cose[1]의 꼭대기에도 0이 있다면 얘내 둘이 연결되면 cycle이 생김
            continue
        union(cost[0], cost[1], root)
        # route.append((cost[0], cost[1]))
        answer += cost[2]

    return answer


# print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4)
# print(solution(4, [[0, 1, 10], [0, 2, 1], [0, 3, 9], [1, 3, 10], [2, 3, 10]]) == 20)
# print(
#     solution(5, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]]) == 7
# )
# print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]) == 8)
print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]]) == 9)
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]) == 104)
# print(
#     solution(
#         6,
#         [
#             [0, 1, 5],
#             [0, 3, 2],
#             [0, 4, 3],
#             [1, 4, 1],
#             [3, 4, 10],
#             [1, 2, 2],
#             [2, 5, 3],
#             [4, 5, 4],
#         ],
#     )
#     == 11
# )
# print(solution(5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]) == 6)
print(solution(5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]) == 8)
print(solution(5, [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]]) == 8)
