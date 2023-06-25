def solution(scores):
    answer = 1
    scores[0].append(-1)
    wanoscore = scores[0][0] + scores[0][1]
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxscore0, maxscore1 = -1, -1
    # print(scores)
    for score in scores:
        if score[0] < maxscore0 and score[1] < maxscore1:
            if score[-1] == -1:
                return -1
            else:
                pass
        else:
            if wanoscore < score[0] + score[1]:
                answer += 1
        maxscore0, maxscore1 = max(maxscore0, score[0]), max(maxscore1, score[1])

    return answer
