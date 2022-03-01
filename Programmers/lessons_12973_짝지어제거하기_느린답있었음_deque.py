from collections import deque


def solution(S):
    answer = -1
    stack = deque([])

    for i, v in enumerate(S):
        if stack:
            if stack[-1] == v:
                stack.pop()
            else:
                stack.append(v)
        else:
            stack.append(v)
    # print(stack)

    if stack:
        answer = 0
    else:
        answer = 1

    return answer


print(solution("baabaa") == 1)
print(solution("cdcd") == 0)
