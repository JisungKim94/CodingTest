def numof(num_):
    cnt = 0
    for i in range(1, num_ + 1):
        if (num_ % i) == 0:
            cnt = cnt + 1
    return cnt


def solution(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        if numof(i) % 2 == 0:
            answer = answer + i
        if numof(i) % 2 == 1:
            answer = answer - i
    return answer


print(solution(13, 17) == 43)
print(solution(24, 27) == 52)
