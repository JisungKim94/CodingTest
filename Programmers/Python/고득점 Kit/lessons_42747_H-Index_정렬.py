def solution(citations):
    answer = 0
    n = len(citations)
    citations = sorted(citations, reverse=1)
    for i, v in enumerate(citations):
        if v <= i:
            answer = i
            break
        else:
            answer = answer + 1

    print(answer)
    return answer


print(solution([3, 0, 6, 1, 5]) == 3)
print(solution([9, 7, 6, 2, 1]) == 3)
print(solution([10, 8, 5, 4, 3]) == 4)
print(solution([25, 8, 5, 3, 3]) == 3)
print(solution([5, 4]) == 2)
