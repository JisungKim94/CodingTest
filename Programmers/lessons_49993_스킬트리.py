def solution(skill, skill_trees):
    answer = 0
    temp = []
    cnt = 0
    for i in skill_trees:
        for j in i:
            if j == skill[cnt]:
                temp.append(skill[cnt])
                if cnt < len(skill) - 1:
                    cnt = cnt + 1
            elif j in skill:
                answer = answer - 1
                break
        answer = answer + 1
        temp = []
        cnt = 0
    print(answer)
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]) == 2)
