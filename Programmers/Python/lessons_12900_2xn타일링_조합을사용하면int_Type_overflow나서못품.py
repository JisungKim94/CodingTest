def solution(n):
    a = 1
    b = 1
    # 점화식 세워서 풀면 댐
    for i in range(n - 1):
        c = (a + b) % 1000000007
        c = int(c)
        a = b
        b = c
    return b


print(solution(4) == 5)
print(solution(5) == 8)
print(solution(6) == 13)
print(solution(7) == 21)
