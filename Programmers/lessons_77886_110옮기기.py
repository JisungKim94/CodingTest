import collections


def solution(s):
    answer = []

    for s_ in s:
        # 110 지우는법... 몰라서 하루종일 못 품 ㅠㅠ
        stack = []
        numof110 = 0
        for str_ in s_:
            # 110이 나온 경우
            if (
                len(stack) >= 2
                and stack[-1] == "1"
                and stack[-2] == "1"
                and str_ == "0"
            ):
                numof110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(str_)

        stack = collections.deque(stack)
        tmp = collections.deque()
        n = len(stack)
        # print(numof110, tmp,stack)
        for i in range(n - 1, -1, -1):
            if stack[i] == "0":
                # print(numof110,tmp,stack)
                while numof110 > 0:
                    tmp.appendleft("0")
                    tmp.appendleft("1")
                    tmp.appendleft("1")
                    numof110 -= 1
                break
            else:
                tmp.append(stack.pop())

        # print(numof110,tmp,stack)

        while stack:
            tmp.appendleft(stack.pop())

        while numof110 > 0:
            tmp.appendleft("0")
            tmp.appendleft("1")
            tmp.appendleft("1")
            numof110 -= 1
        # print(numof110,tmp,stack)

        answer.append("".join(tmp))
    return answer
