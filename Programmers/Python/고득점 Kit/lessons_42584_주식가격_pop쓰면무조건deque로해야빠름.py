import collections


def solution(prices):
    answer = [0] * len(prices)
    stack = collections.deque(prices)
    cnt = 0
    while stack:
        temp = stack.popleft()
        for i, v in enumerate(stack):
            if temp > v:
                answer[cnt] = i + 1
                break
            else:
                answer[cnt] = i + 1
        cnt = cnt + 1

    # print(answer)

    return answer


print(solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])
print(solution([5, 4, 3, 2, 1]) == [1, 1, 1, 1, 0])
print(solution([5, 1, 1, 1, 5]) == [1, 3, 2, 1, 0])
