def solution(n):
    answer = 1
    if n == 1:
        return answer
    temp = 0
    pretemp = 0
    prepretemp = 0
    preprepretemp = 0
    cnt = 0
    for i in range(1, n):
        temp += i
        if n < temp:
            break
        cnt += 1
        preprepretemp = prepretemp
        prepretemp = pretemp
        pretemp = temp
    # print(n, pretemp, prepretemp, cnt)
    answer = max((n - prepretemp) * cnt, (n - preprepretemp) * (cnt - 1))
    # print(answer)
    return answer


print(solution(1) == 1)  # 1 1
print(solution(2) == 2)  # 2 2
print(solution(3) == 4)  # 21 4
print(solution(4) == 6)  # 31 6
print(solution(5) == 8)  # 41 8
print(solution(6) == 10)  # 51 10 321 9
print(solution(7) == 12)  # 61 12 421 12
print(solution(8) == 15)  # 71 14 521 15
print(solution(9) == 18)  # 81 16 621 18
print(solution(10) == 21)  # 721 21 4321 16
print(solution(11) == 24)  # 821 24 5321 20
print(solution(12) == 27)  # 921 27 6321 24
print(solution(13) == 30)  # 1021 30 7321 28
print(solution(14) == 33)  # 1121 33 8321 32
print(solution(15) == 36)  # 1221 36 9321 36
print(solution(16) == 40)  # 1321 39 10321 40
