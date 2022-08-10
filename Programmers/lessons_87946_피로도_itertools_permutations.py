import itertools


def solution(k, dungeons):
    answer = []
    temp = []
    temp_answer = 0
    # print(list(itertools.permutations(dungeons)))
    for i in list(itertools.permutations(dungeons)):
        k_ = k
        temp_answer = 0
        for j in i:
            if j[0] > k_:
                break
            else:
                k_ = k_ - j[1]
                temp_answer += 1
        answer.append(temp_answer)

    return max(answer)
