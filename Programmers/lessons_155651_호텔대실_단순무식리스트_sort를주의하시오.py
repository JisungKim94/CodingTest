def solution(book_time):
    answer = 0
    room = [[0] * 1450]
    book_time.sort()

    def time_min(time):
        time_s = time[0].split(":")
        time_e = time[1].split(":")
        time_s = int(time_s[0]) * 60 + int(time_s[1])
        time_e = int(time_e[0]) * 60 + int(time_e[1])
        return time_s, time_e

    for time in book_time:
        s, e = time_min(time)
        e = e + 10
        for i in range(len(room)):
            if 1 not in room[i][s:e]:
                add_flag = False
                for j in range(s, e):
                    room[i][j] = 1
                break
            else:
                add_flag = True
        if add_flag:
            room.append([0] * 1450)
            for j in range(s, e):
                room[i + 1][j] = 1
        # print(len(room))

    return len(room)
