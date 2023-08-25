def solution(scores):
    answer = 1
    # 원호 체크용
    scores[0].append(-1)
    wanoscore = scores[0][0] + scores[0][1]

    # 합이 크다는건 둘 다 작을순 없다는 뜻, [0]은 내림차순 [1]은 오름차순 정렬
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxscore0, maxscore1 = scores[0][0], scores[0][1]

    # 정렬을 하나는 내림차순 하나는 오름차순으로 했응게 tc 3번같은 경우
    # 입력값 〉	[[2, 2], [1, 4], [3, 2], [3, 2], [2, 1], [2, 5], [2, 2], [2, 2]]
    # 기댓값 〉	4
    # maxscore0은 업데이트가 안 되지만, 어차피 그 이후에 오는 애들은 임마보다 작은 애들이라 의미없음
    # maxscore1은 업데이트 안 해주면 2,5 같은 애들 처리를 못 해줌 얘는 오름차순 해 놨기 때문에 max만 보면
    # 갑자기 maxscore0,1이 3,5가 되지만(실제론 3,2 혹은 2,5임) maxscore0인 3은 볼 필요가 없움 이미 얘보다 작은 애들을
    # 보고있는 순간이기 때문(내림차순)
    print(scores)
    for score in scores:
        if score[0] < maxscore0 and score[1] < maxscore1:
            if score[-1] == -1:  # 원호면 return -1
                return -1
            else:
                pass
        else:
            if wanoscore < score[0] + score[1]:
                answer += 1
        maxscore1 = max(maxscore1, score[1])
        print(score, maxscore0, maxscore1)

    return answer
