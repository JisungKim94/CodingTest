from itertools import combinations


def solution(number, k):
    answer = ""
    comb = list(combinations(number, len(number) - k))
    temp = ""
    answer_list = []
    for i in comb:
        for j in i:
            temp = temp + j
        answer_list.append(int(temp))
        temp = ""
    # print(answer_list)
    answer = str(max(answer_list))

    return answer


print(solution("1924", 2) == "94")
print(solution("1231234", 3) == "3234")
print(solution("4177252841", 4) == "775841")
