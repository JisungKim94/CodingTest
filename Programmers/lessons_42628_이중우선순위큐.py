import heapq
import collections


def solution(operations):
    operations = collections.deque(operations)
    que = []

    while operations:
        temp = operations.popleft()
        num = int(temp[2:])
        if temp[0] == "I":
            heapq.heappush(que, num)
        elif temp[0 == "D"] and que:
            if num == -1:
                heapq.heappop(que)
            elif num == 1:
                que.pop(que.index(max(que)))

    if not que:
        que = [0, 0]
    que = [max(que), min(que)]
    # print(que)
    return que


# print(solution(["I 16", "D 1"]) == [0, 0])
print(solution(["I 7", "I 5", "I -5", "D -1"]) == [7, 5])
print(solution(["I 7", "I 5", "I -5", "D 1"]) == [5, -5])
