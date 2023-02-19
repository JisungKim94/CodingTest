def solution(k, tangerine):
    answer = 0
    dic = dict.fromkeys(set(tangerine))
    # print(dic)
    for i in tangerine:
        if dic[i] == None:
            dic[i] = 1
        else:
            dic[i] = dic[i] + 1
    dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    # print(dic)
    for i in dic:
        k = k - i[1]
        answer = answer + 1
        if k <= 0:
            break

    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]) == 3)
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]) == 2)
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]) == 1)
