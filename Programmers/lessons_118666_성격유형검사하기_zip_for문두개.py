from collections import defaultdict


def solution(survey, choices):
    answer = ""
    dic = defaultdict(int)
    # dic = {}
    for i in survey:
        dic[i[0]] = 0
        dic[i[1]] = 0

    for i, j in zip(survey, choices):
        if j == 1:
            dic[i[0]] += 3
        elif j == 2:
            dic[i[0]] += 2
        elif j == 3:
            dic[i[0]] += 1
        elif j == 4:
            pass
        elif j == 5:
            dic[i[1]] += 1
        elif j == 6:
            dic[i[1]] += 2
        elif j == 7:
            dic[i[1]] += 3

    if dic["T"] > dic["R"]:
        answer = answer + "T"
    else:
        answer = answer + "R"
    if dic["F"] > dic["C"]:
        answer = answer + "F"
    else:
        answer = answer + "C"
    if dic["M"] > dic["J"]:
        answer = answer + "M"
    else:
        answer = answer + "J"
    if dic["N"] > dic["A"]:
        answer = answer + "N"
    else:
        answer = answer + "A"
    # print(dic)
    # print(answer)
    return answer


# print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]) == "TCMA")
print(solution(["TR", "RT", "TR"], [7, 1, 3]) == "RCJA")
