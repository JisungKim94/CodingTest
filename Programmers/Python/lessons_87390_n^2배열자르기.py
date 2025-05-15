def solution(n, left, right):
    answer = [0] * (right - left + 1)

    print("1차원 배열길이 :", n**2)
    print("행, 열 기준 시작점", (left // n), (left % n))
    print("행, 열 기준 최종점", (right // n), (right % n))

    print(
        (7 // n) + 1,
        (7 % n) + 1,
        (8 // n) + 1,
        (8 % n) + 1,
        (9 // n) + 1,
        (9 % n) + 1,
        (10 // n) + 1,
        (10 % n) + 1,
        (11 // n) + 1,
        (11 % n) + 1,
    )

    for i, v in enumerate(range(left, right + 1, 1)):
        if ((v // n) + 1) >= ((v % n) + 1):
            temp = (v // n) + 1
        else:
            temp = (v % n) + 1
        answer[i] = temp
    print(answer)

    return answer


print(solution(3, 2, 5) == [3, 2, 2, 3])
print(solution(4, 7, 14) == [4, 3, 3, 3, 4, 4, 4, 4])
