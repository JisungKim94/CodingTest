def solution(d, budget):
    answer = 0
    temp = 0
    d = sorted(d)

    for d_ in d:
        temp = temp + d_
        if temp <= budget:
            answer = answer + 1
    # print(answer)

    return answer


print(solution([1, 3, 2, 5, 4], 9) == 3)
print(solution([2, 2, 3, 3], 10) == 4)
