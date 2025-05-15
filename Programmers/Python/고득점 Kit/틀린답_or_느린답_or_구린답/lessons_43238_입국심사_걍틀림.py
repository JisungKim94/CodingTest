n = 6
times = [7, 10]


def solution(n, times):
    is_people_remain = True
    time_cnt = 0
    times = sorted(times)
    times = list(zip(times, [1] * len(times)))
    very_left_times = times.pop(0)
    times.append(very_left_times)
    n = n - len(times)
    while is_people_remain == True:
        time_cnt = time_cnt + 1
        if time_cnt % very_left_times[0] == 0:
            if times[0][0] < very_left_times[0] and very_left_times[1] == 0:
                time_cnt = time_cnt + (times[0][0] - (time_cnt % times[0][0]))
            elif times[0][0] > very_left_times[0] and very_left_times[1] == 0:
                very_left_times = times.pop(0)
                very_left_times[1] = 0
                times.append(very_left_times)
            n = n - 1
        if n == 0:
            is_people_remain = False

    return time_cnt


print(solution(n, times))
