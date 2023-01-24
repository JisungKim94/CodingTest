import heapq


def solution(A, B):
    answer = 0
    temp = []
    heapq.heapify(A)
    for i in B:
        heapq.heappush(temp, -i)

    while A:
        answer = answer + (heapq.heappop(A) * -heapq.heappop(temp))

    return answer


print(solution([1, 4, 2], [5, 4, 4]) == 29)
print(solution([1, 2], [3, 4]) == 10)
