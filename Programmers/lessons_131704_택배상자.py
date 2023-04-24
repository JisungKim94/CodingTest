import collections


def solution(order):
    answer = 0
    boxs = collections.deque(list(range(1, len(order) + 1)))
    order = collections.deque(order)
    filo = collections.deque([])

    while boxs and order:
        if boxs[0] == order[0]:
            boxs.popleft()
            order.popleft()
            answer = answer + 1
            while filo and filo[-1] == order[0]:
                filo.pop()
                order.popleft()
                answer = answer + 1
        else:
            filo.append(boxs.popleft())

    while filo:
        if filo.pop() == order.popleft():
            answer = answer + 1
        else:
            break
    return answer


print(solution([4, 3, 1, 2, 5]) == 2)
print(solution([5, 4, 3, 2, 1]) == 5)
print(solution([1, 2, 3, 4, 5]) == 5)
