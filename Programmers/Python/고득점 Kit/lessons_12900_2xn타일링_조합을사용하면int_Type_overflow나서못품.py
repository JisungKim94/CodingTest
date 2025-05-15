def comb(f, r):
    num = 1
    den = 1
    for i in range(f, f - r, -1):
        num *= i
    for i in range(r, 0, -1):
        den *= i
    return int(num / den)


def solution(n):
    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    else:
        if n % 2 == 0:
            cnt = 2
            answer = 2
            starting = int(n / 2 + 1)
            end = n - 1
            for i in range(starting, end + 1, 1):
                answer += comb(i, cnt)
                cnt = cnt + 2
        else:
            answer = 1
            cnt = 1
            starting = int(n / 2 + 1)
            end = n - 1
            for i in range(starting, end + 1, 1):
                answer += comb(i, cnt)
                cnt = cnt + 2

    return answer % 1000000007


print(solution(4) == 5)
print(solution(5) == 8)
print(solution(6) == 13)
print(solution(7) == 21)
