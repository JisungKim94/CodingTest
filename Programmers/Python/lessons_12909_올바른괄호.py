import collections


def solution(s):
    answer = True
    que = collections.deque([])

    for i in s:
        if i == "(":
            que.append(1)
        else:
            try:
                que.pop()
            except:
                return False

    if que:
        answer = False
    else:
        answer = True
    # print(que)
    return answer


# print(solution("()()") == True)
# print(solution("(())()") == True)
# print(solution(")()(") == False)
# print(solution("(()(") == False)
# print(solution("())(()") == False)
print(solution("(())))))))))") == False)
