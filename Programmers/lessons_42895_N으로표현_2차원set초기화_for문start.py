def solution(N, number):

    answer = -1
    # 2차원 set 초기화
    # 공부할 때 참고하라고 list 초기화 하는법도 써둠
    # list_temp = [[0] * 8 for i in range(8)]
    # list_temp[0][0] = 1
    # print(list_temp)
    sets = [set() for _ in range(8)]
    pre_sets = {}
    # i = 0 일 경우 error 발생해서 아래와 같이 만들거나
    # enumerate 사용 해야 함
    # for i in range(8):
    # sets[i].add(int(str(N) * (i + 1)))

    for i, x in enumerate(sets, start=1):
        for j in pre_sets:
            x.add(j)
        x.add(int(str(N) * i))
        x.add((int(str(2 * N)) + int(str(-N)) * i))
        x.add((int(str(N)) + int(str(N)) * (i - 1)))
        x.add(
            int((int(str(N)) / int(str(N)) * (i - 1)))
        )  # 이거 소수 피하려고 int 조랄 안하고 // 로 쓰면 깔끔했음
        x.add(int((int(str(N)) * int(str(N)) * (i - 1))))
        pre_sets = x

    print(sets)
    # 5개로 만들 수 있는 case 구할 때 4개 + 1개 로 구했는데,
    # 3개 + 2개 같은 case도 고려해야함 그렇게 수정한게 아래 보이는 모양
    for i in range(1, 8):
        for j in range(i):
            for op1 in sets[j]:
                for op2 in sets[i - j - 1]:
                    sets[i].add(op1 + op2)
                    sets[i].add(op1 - op2)
                    sets[i].add(op1 * op2)
                    if op2 != 0:
                        sets[i].add(op1 // op2)
    # print(sets)
    for i, v in enumerate(sets):
        if number in v:
            answer = i + 1
            break

    # print(answer)

    return answer


# print(solution(5, 12) == 4)
# print(solution(2, 11) == 3)
print(solution(8, 53) == 5)


""" 
5 1개 : 5
5 2개 : 55 (55),     10 (5+5),       0(5-5),         1 (5/5),        25 (5*5)
5 3개 : 555 (555),      15 (5+5+5),     -5 (5-5-5),     not int,        125 (5*5*5), 에다가 위에 2개 짜리에 5 사칙연산 한 개 씩
5 4개 : 위에꺼 반복
"""
