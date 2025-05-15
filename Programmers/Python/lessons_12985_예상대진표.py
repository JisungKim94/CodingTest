def solution(n, a, b):
    answer = 0
    while a != b:
        answer = answer + 1
        # // 몫
        a, b = (a + 1) // 2, (b + 1) // 2

    return answer


print(solution(8, 4, 5) == 3)
print(solution(8, 2, 3) == 2)
print(solution(16, 8, 9) == 4)
print(solution(16, 9, 12) == 2)
