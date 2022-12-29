import collections

def solution(topping):
    answer = 0
    chul = set()
    dong = collections.Counter(topping)
    
    # temp in chul 이런식으로 하면 시간초과 난다.
    # in이 Counter 쓰는거보다 느린가봉가
    # for _ in range(len(topping)):
    #     temp = dong.pop()
    #     if temp in chul:
    #         pass
    #     else:
    #         chul.append(temp)
    #     if temp in dong:
    #         pass
    #     else:
    #         d = d -1
    #     if len(chul) == d:
    #         answer = answer + 1
    #   print(chul,d)
    
    #  Counter 써서 풀기
    for i in range(len(topping)):
        temp = topping[i]
        chul.add(temp)

        if dong[temp] > 1:
            dong[temp] = dong[temp] - 1
        else:
            del dong[temp]

        if len(chul) == len(dong):
            answer = answer + 1

    # print(answer)
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2])==2)
print(solution([1, 2, 3, 1, 4])==0)