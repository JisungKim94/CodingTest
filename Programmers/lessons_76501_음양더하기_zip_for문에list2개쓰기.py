def solution(absolutes, signs):
    answer = 0

    for abs_, sings_ in zip(absolutes, signs):
        if sings_ == True:
            answer = answer + abs_
        else:
            answer = answer - abs_

    return answer


print(solution([4, 7, 12], [True, False, True]) == 9)
print(solution([1, 2, 3], [False, False, True]) == 0)
