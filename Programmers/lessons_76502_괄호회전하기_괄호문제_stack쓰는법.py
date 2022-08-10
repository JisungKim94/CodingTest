from collections import deque


def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        # print(s)
        tmp = s.pop()
        s.appendleft(tmp)
        if is_valid(s):
            answer = answer + 1

    # print(answer)
    return answer


def is_valid(s):
    s_ = s.copy()
    left = ["(", "{", "["]
    right = [")", "}", "]"]
    stack = []
    for letter in s_:
        if letter in left:
            stack.append(letter)
        elif letter in right:
            if len(stack) <= 0:
                return False
            if left.index(stack.pop()) != right.index(letter):
                return False
    return len(stack) == 0


# print(solution("[](){}") == 3)
# print(solution("}]()[{") == 2)
# print(solution("[)(]") == 0)
# print(solution("}}}") == 0)
# print(solution("([{)}]") == 1)
print(solution("[(])") == 0)
