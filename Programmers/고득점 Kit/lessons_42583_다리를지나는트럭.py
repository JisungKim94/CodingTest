from collections import deque
import copy


def solution(bridge_length, weight, truck_weights):
    cnt = 0

    crossed = deque([])
    crossing = deque([])
    entrytime = deque([])
    waiting = deque(copy.deepcopy(truck_weights))
    while len(crossed) < len(truck_weights):
        cnt = cnt + 1
        for i, v in enumerate(entrytime):
            if cnt - v >= bridge_length:
                entrytime.popleft()
                crossed.append(crossing.popleft())
                break
        # for i, v in enumerate(waiting):
        if waiting:
            if weight - sum(crossing) >= waiting[0]:
                crossing.append(waiting.popleft())
                entrytime.append(cnt)
    print(cnt)
    return cnt


# print(solution(2, 7, [7, 4, 5, 6]) == 8)
# print(solution(100, 100, [10]) == 101)
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110)
# print(solution(1, 2, [1, 1, 1]) == 4)

print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]) == 19)
print(solution(5, 5, [1, 1, 1, 1, 1, 2, 2]) == 14)
