from collections import deque


def solution(n, t, m, timetable):
    answer = 0
    timetable_ = deque([])
    for i in timetable:
        i = i.split(":")
        timetable_.append(int(i[0]) * 60 + int(i[1]))
    timetable_ = sorted(timetable_)

    arrivedtime = 540
    endtime = t * (n - 1) + 540
    cnt = 0
    if timetable_[0] > endtime:
        answer = endtime
    else:
        while timetable_:
            if timetable_[0] <= arrivedtime and cnt < m:
                if arrivedtime == endtime and cnt == (m - 1):
                    break
                timetable_.pop(0)
                cnt = cnt + 1
            else:
                cnt = 0
                arrivedtime = arrivedtime + t
                if arrivedtime > endtime:
                    break
        if timetable_:
            if timetable_[0] > endtime:
                answer = endtime
            else:
                answer = timetable_[0] - 1
        else:
            answer = endtime

    HH = "0" + str(answer // 60) if answer // 60 < 10 else str(answer // 60)
    MM = "0" + str(answer % 60) if answer % 60 < 10 else str(answer % 60)
    answer = HH + ":" + MM
    return answer
