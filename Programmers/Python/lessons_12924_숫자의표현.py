def checker(start, stop):
    return sum(range(start, stop, 1))


def solution(n):
    answer = 0

    for start in range(1, int(n / 2) + 1):
        for length in range(141):
            temp = checker(start, start + length)
            if n == temp:
                answer = answer + 1
                break
            elif n < temp:
                break
    answer = answer + 1
    return answer


print(solution(15) == 4)
