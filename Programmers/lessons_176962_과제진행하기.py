def hmtom(hm):
    hm = hm.split(":")
    h, m = int(hm[0]), int(hm[1])
    return h * 60 + m


def solution(plans):
    answer = []
    waiting = []
    for i in plans:
        i[1] = hmtom(i[1])
        i[2] = int(i[2])
    plans.sort(key=lambda x: x[1])

    for i, v in enumerate(plans):
        if i + 1 < len(plans):
            freetime = plans[i + 1][1] - v[1]
        else:
            freetime = 100001
        # print(freetime,v[2])
        if freetime >= v[2]:
            answer.append(v[0])
            freetime = freetime - v[2]
            while freetime > 0 and waiting:
                # print(freetime,waiting)
                temp = waiting.pop()
                if temp[1] - freetime > 0:
                    temp[1] = temp[1] - freetime
                    freetime = 0
                    waiting.append(temp)
                else:
                    answer.append(temp[0])
                    freetime = freetime - temp[1]

        else:
            waiting.append([v[0], v[2] - freetime])
        # print(answer,waiting)

    return answer
