def solution(s):
    answer = ""

    s = s.split(" ")
    tmp = []
    for i in s:
        i = int(i)
        tmp.append(i)

    # print(min(tmp), max(tmp))
    answer = str(min(tmp)) + " " + str(max(tmp))
    # print(answer)
    return answer


print(solution("1 2 3 4") == "1 4")
print(solution("-1 -2 -3 -4") == "-4 -1")
print(solution("-1 -1") == "-1 -1")
