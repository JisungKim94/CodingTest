import heapq

def solution(n, k, enemy):
    answer = 0
    # 주어진 list heap으로 만드는 법
    tempheap = enemy[:k]
    heapq.heapify(tempheap)
    # 나 맨날 이래 썼는데 ㅠㅠ
    # tempheap = []
    # for i in range(k):
    #     heapq.heappush(tempheap, enemy[i])

    if k >= len(enemy):
        return len(enemy)
    if n >= sum(enemy):
        return len(enemy)

    for i in range(k, len(enemy)):
        # heappop
        # If you use pop[0] instead of heappop, it doesn't work properly.
        # if you use like "local_summation.pop(local_summation[0])" min-heap are not available.
        heapq.heappush(tempheap, enemy[i])
        n = n - heapq.heappop(tempheap)
        if n < 0:
            return i

    return len(enemy)


print(solution(7,3,[4, 2, 4, 5, 3, 3, 1])==5)
# print(solution(7,3,[1, 1, 1, 1, 10, 10, 10])==7)
# print(solution(7,3,[5, 1, 1, 1, 10, 10, 10])==6)
# print(solution(7,3,[1, 1, 1, 10, 10, 10, 10])==6)
# print(solution(7,3,[6, 1, 1, 10, 10, 10, 10])==5)
# print(solution(7,3,[10, 10, 10, 10, 10, 10, 10])==3)
# print(solution(7,3,[10, 10, 10, 1, 1, 1, 1])==7)
# print(solution(7,3,[1, 10, 1, 10, 1, 10, 1])==7)
# print(solution(7,3,[4, 3, 1, 4, 3, 1, 1])==7)
# print(solution(2,4,[3,3,3,3])==4)
# print(solution(7,3,[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])==10)
# print(solution(3,3,[1, 2, 3, 1, 10, 1])==6)
# print(solution(3,3,[1, 0, 0, 1, 0, 1])==6)