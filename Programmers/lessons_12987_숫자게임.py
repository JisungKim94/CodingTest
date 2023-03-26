from collections import deque

# 걍 list로 할때 deque랑 속도차이 1/12
def solution(A, B):
    answer = 0
    A = deque(sorted(A, reverse=1))
    B = deque(sorted(B, reverse=1))
    # print(A, B)
    for idx, val in enumerate(A):
        if val >= B[0]:
            B.pop()
        else:
            B.popleft()
            answer = answer + 1

    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]) == 3)
print(solution([5, 1, 3, 7], [2, 2, 4, 4]) == 2)
print(solution([3, 1, 3, 7], [2, 2, 4, 4]) == 3)
# print(solution([2, 2, 2, 2], [1, 1, 1, 1]) == 0)
