def solution(numbers):
    answer = ""
    temp_0 = []
    temp_1 = []
    for i, v in enumerate(numbers):
        temp_0.append([str(v), i])
    for i, v in enumerate(temp_0):
        length = len(v[0])
        v[0] = v[0] + v[0] * (4 - length)
    # print(temp_0)
    temp_0 = sorted(temp_0, reverse=True)
    # print(temp_0)

    for j in temp_0:
        temp_1.append(str(numbers[j[1]]))
        answer = answer + str(numbers[j[1]])

    # 0000 같은 조건 처리 0000 -> 0
    answer = str(int(answer))

    return answer


# print(solution([6, 10, 2]))
# print(solution([67, 676, 677]))  # 67767676
print(solution([0, 0, 0, 0]))
