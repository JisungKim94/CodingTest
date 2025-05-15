import heapq


def solution(n, works):
    answer = 0
    heap = []

    for i in works:
        heapq.heappush(heap, -i)  # (우선 순위, 값)
    # print(heap)
    while n > 0:
        temp = heapq.heappop(heap)
        if temp >= 0:
            break
        temp = temp + 1
        heapq.heappush(heap, temp)
        n = n - 1

    # print(heap)
    for i in heap:
        answer = answer + i**2

    # print(heap)

    return answer


print(solution(4, [4, 3, 3]) == 12)
print(solution(1, [2, 1, 2]) == 6)
print(solution(3, [1, 1]) == 0)
# print(solution(1000000, [50] * 20000) == 0)
