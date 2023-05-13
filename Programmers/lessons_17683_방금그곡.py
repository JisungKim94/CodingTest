def solution(m, musicinfos):
    answer = []
    playingtime = 0
    temp_m = []
    for m_ in m:
        if m_ == "#":
            temp_m[-1] = temp_m[-1] + "#"
        else:
            temp_m.append(m_)
    # print(temp_m)
    cnt = 0
    for i in musicinfos:
        i = i.split(",")
        sttime, endtime = i[0], i[1]
        hour = int(endtime[0:2]) - int(sttime[0:2])
        minute = int(endtime[3:5]) - int(sttime[3:5])
        while hour > 0:
            hour = hour - 1
            minute = minute + 60
        playingtime = minute

        melody = []
        for j in i[3]:
            if j == "#":
                melody[-1] = melody[-1] + "#"
            else:
                melody.append(j)

        temp = ""
        if playingtime // len(melody) != 0:
            temp = (
                melody * (playingtime // len(melody))
                + melody[: playingtime % len(melody)]
            )
        else:
            temp = melody[:playingtime]
        # print(melody,temp)
        # print(temp,temp_m)
        # print(len(temp)-len(temp_m))

        for k in range(len(temp) - len(temp_m) + 1):
            # print(temp[k:len(temp_m)+k])
            if temp[k : len(temp_m) + k] == temp_m:
                answer.append([playingtime, i[2], cnt])
                break
        cnt = cnt - 1

    answer.sort(key=lambda x: (x[0], x[2]), reverse=1)
    # print(answer)
    if answer:
        return answer[0][1]
    else:
        return "(None)"
