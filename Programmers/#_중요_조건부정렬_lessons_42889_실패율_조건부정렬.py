def solution(N, stages):
    answer = []
    temp_answer = []
    failrate = 0.0
    cnt_den = 0
    cnt_nom = 0

    for i in range(N):
        for stage in stages:
            if stage >= i + 1:
                cnt_den = cnt_den + 1
                if stage == i + 1:
                    cnt_nom = cnt_nom + 1
        try:
            failrate = cnt_nom / cnt_den
        except:
            ZeroDivisionError()
            failrate = 0.0
        temp_answer.append([failrate, i + 1])
        failrate = 0.0
        cnt_nom = 0
        cnt_den = 0

    # ====================== 조건부 정렬 =================================
    print(temp_answer)
    # lamda식을 통해 다중 조건 정렬을 쓸 수 있다.
    # key = lambda x:(-x[0], x[1]) 은 먼저 0번째 값으로 내림차순(-1 붙여서)
    # 정렬을 하고 1번째 값으로 오름차순(default) 정렬을 한다
    temp_answer = sorted(temp_answer, key=lambda x: (-x[0], x[1]))
    print(temp_answer)
    # ====================== 조건부 정렬 =================================

    for i, j in temp_answer:
        answer.append(j)

    # print(answer)
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5])
print(solution(5, [4, 4, 4, 4, 4]) == [4, 1, 2, 3])


# 더 좋은 답 (훔쳤음 ㅋ)
# def solution(N, stages):
#     answer = []
#     fail = []
#     info = [0] * (N + 2)
#     for stage in stages:
#         info[stage] += 1
#     for i in range(N):
#         be = sum(info[(i + 1):])
#         yet = info[i + 1]
#         if be == 0:
#             fail.append((str(i + 1), 0))
#         else:
#             fail.append((str(i + 1), yet / be))
#     for item in sorted(fail, key=lambda x: x[1], reverse=True):
#         answer.append(int(item[0]))
#     return answer
