import math


def solution(n, s):
    answer = []
    temp = math.floor(s / n)
    if temp == 0:
        return [-1]
    answer.append(temp)
    answer = answer * n

    indice = s - sum(answer)
    for i in range(indice):
        i = i + 1
        answer[-i] = temp + 1
    # while sum(answer) != s:
    # answer[-i] = answer[-i] + 1
    # i = i + 1
    print(answer)
    return answer


print(solution(2, 9) == [4, 5])
print(solution(2, 1) == [-1])
print(solution(2, 8) == [4, 4])
print(solution(2, 7) == [3, 4])
print(solution(3, 7) == [2, 2, 3])
