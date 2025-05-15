def solution(S):
    answer = -1
    checker = True
    S = [i for i in S]
    while S and checker == True:
        checker = False
        preS = ""
        for i, v in enumerate(S):
            if v == preS:
                S.pop(i - 1)
                S.pop(i - 1)
                checker = True
                break
            else:
                preS = v

    if S:
        answer = 0
    else:
        answer = 1

    return answer


print(solution("baabaa") == 1)
print(solution("cdcd") == 0)
