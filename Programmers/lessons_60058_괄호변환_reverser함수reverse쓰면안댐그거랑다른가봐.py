from collections import deque


def reverser(p):
    if p == ")":
        return "("
    else:
        return ")"


def checker(p):
    stack_u = deque()
    stack_v = deque()
    cnt_left = 0
    cnt_right = 0
    first_run = True

    if len(p) != 0:
        for i in p:
            if cnt_left == cnt_right and first_run == False:
                stack_v.append(i)
                continue
            if i == "(":
                cnt_left = cnt_left + 1
                stack_u.append(i)
                first_run = False
            else:
                cnt_right = cnt_right + 1
                stack_u.append(i)
                first_run = False
    else:
        return ""

    if stack_u[0] == "(":
        return "".join(stack_u) + checker(stack_v)
    else:
        temp = "("
        temp = temp + checker(stack_v) + ")"
        stack_u.popleft()
        stack_u.pop()
        for idx, val in enumerate(stack_u):
            stack_u[idx] = reverser(val)
        temp = temp + "".join(stack_u)
        # print(temp)
        return temp


def solution(p):
    answer = ""
    answer = checker(p)
    # print(answer)
    return answer


# print(solution("(()())()") == "(()())()")
# print(solution(")(") == "()")
# print(solution("()))((()") == "()(())()")
