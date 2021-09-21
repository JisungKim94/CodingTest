# progresses = [93, 30, 55]
progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 30, 5]
speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses_, speeds_):
    answer = []
    day_cnt = 0
    return_cnt = 0

    # python에선 list가 []면 false를 retrun 공백 list가 아니면 true를 return
    while progresses_:
        for i in range(len(progresses_)):
            progresses_[i] = progresses_[i] + speeds_[i]

        # python에선 list가 []면 false를 retrun 공백 list가 아니면 true를 return
        if progresses_:
            while progresses_[0] >= 100:
                progresses_.pop(0)
                speeds_.pop(0)
                return_cnt = return_cnt + 1
                # python에선 list가 []면 false를 retrun 공백 list가 아니면 true를 return
                if progresses_:
                    if not progresses_[0] >= 100:
                        answer.append(return_cnt)
                        return_cnt = 0
                else:
                    answer.append(return_cnt)
                    break

        day_cnt = day_cnt + 1
    return answer


print(solution(progresses, speeds))
