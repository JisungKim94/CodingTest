def solution(s):
    answer = []
    j = -1
    # print(s)
    # s = s.replace("{", "")
    # print(s)
    # s = s.replace("}", "")
    # print(s)
    # s = list(s.split(","))
    # print(s)
    # s = sorted(s, key=lambda x: len(x))
    # print(s)

    # 위 과정을 한 번에 하는 법
    s = s[2:-2]
    s = sorted(s.split("},{"), key=lambda x: len(x))
    # print(s)

    for idx, val in enumerate(s):
        i = val.split(",")
        for j in i:
            j_ = int(j)
            if j_ not in answer:
                answer.append(j_)

        # if i not in answer:
        # answer.append(j)

    # print(answer)
    return answer


# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4])
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}") == [2, 1, 3, 4])
print(solution("{{20,111},{111}}") == [111, 20])
# print(solution("{{123}}") == [123])
# print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}") == [3, 2, 4, 1])
