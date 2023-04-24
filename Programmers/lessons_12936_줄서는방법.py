import math

# import itertools


def solution(n, k):
    answer = []
    temp = list(range(1, n + 1))
    # temp = list(itertools.permutations(temp))
    # print(temp)

    n = n - 1
    k = k - 1
    info = []
    while n > 0:
        fac = math.factorial(n)
        info.append((k // fac, k % fac))
        # print(fac,info)
        n = n - 1
        k = k - fac * (k // fac)

    # print(temp)
    for i, v in enumerate(info):
        answer.append(temp[v[0]])
        temp.remove(temp[v[0]])
    answer.append(temp[0])
    return answer


print(solution(4, 11) == [2, 4, 1, 3])
print(solution(4, 12) == [2, 4, 3, 1])
