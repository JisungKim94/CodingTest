from collections import deque


def solution(queue1, queue2):
    answer = -2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    length = len(queue1)
    cnt = 0
    sumque1 = sum(queue1)
    sumque2 = sum(queue2)

    for _ in range(len(queue1) * 3):
        if sumque1 > sumque2:
            temp = queue1.popleft()
            sumque1 = sumque1 - temp
            sumque2 = sumque2 + temp
            queue2.append(temp)
        elif sumque1 < sumque2:
            temp = queue2.popleft()
            sumque1 = sumque1 + temp
            sumque2 = sumque2 - temp
            queue1.append(temp)
        else:
            break
        cnt = cnt + 1

    if cnt >= length * 2:
        answer = -1
    else:
        answer = cnt

    print(cnt)
    print(answer)
    return answer


# print(solution([3, 2, 7, 2], [4, 6, 5, 1]) == 2)
# print(
#     solution(
#         [
#             1,
#             2,
#             1,
#             2,
#         ],
#         [1, 10, 1, 2],
#     )
#     == 7
# )
# print(solution([1, 1], [1, 5]) == -1)
print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1)
