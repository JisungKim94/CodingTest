def Fibonacci(prepre, pre, cnt, n, answer):
    cnt = cnt + 1
    if cnt >= n - 1:
        return pre + prepre
    else:
        return Fibonacci(pre, prepre + pre, cnt, n, answer)


def solution(n):
    # 재귀함수로 못 품 (max depth 문제)
    answer = 0
    # cnt = 0
    # answer = Fibonacci(0, 1, cnt, n, answer)

    fibo = []
    for num in range(0, n + 1):
        if num == 0:
            fibo.append(0)
        elif num == 1:
            fibo.append(1)
        else:
            fibo.append(fibo[num - 2] + fibo[num - 1])

    return fibo[n] % 1234567
    # return answer % 1234567


print(solution(3) == 2)
print(solution(5) == 5)
# python max depth 문제가 있네 재귀함수로는 못 품
print(solution(100000) == 0)
