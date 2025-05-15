def convert(num, base):
    tmp = "0123456789ABCDEF"
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    answer = ""
    temp = ""
    for i in range(t * m):
        temp = temp + convert(i, n)
    # print(temp)

    cnt = 0
    for idx, v in enumerate(temp):
        if (idx % m + 1) == p and (cnt < t):
            answer = answer + v
            cnt = cnt + 1
    return answer


print(solution(2, 4, 2, 1) == "0111")
print(solution(16, 16, 2, 1) == "02468ACE11111111")
print(solution(16, 16, 2, 2) == "13579BDF01234567")
