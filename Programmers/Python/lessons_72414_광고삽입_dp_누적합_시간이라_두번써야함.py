def str_to_int(time):
    h, m, s = time.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = "0" + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = "0" + str(m) if m < 10 else str(m)
    time = time % 60
    s = "0" + str(time) if time < 10 else str(time)
    return h + ":" + m + ":" + s


def solution(play_time, adv_time, logs):
    play_st, play_end = 0, str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    dp = [0] * (play_end + 1)
    normalized_logs = []
    for log in logs:
        st, end = log.split("-")
        st, end = str_to_int(st), str_to_int(end)
        normalized_logs.append((st, end))

    for st, end in normalized_logs:
        dp[st] += 1
        dp[end] -= 1
    for i in range(1, len(dp)):
        dp[i] = dp[i] + dp[i - 1]
    for i in range(1, len(dp)):
        dp[i] = dp[i] + dp[i - 1]
    maxviewtime = 0
    idx = 0
    for i in range(len(dp)):
        if (i + adv_time) >= play_end:
            if dp[-1] - dp[i] > maxviewtime:
                idx = i + 1
                maxviewtime = dp[play_end] - dp[i]
        else:
            if dp[i + adv_time] - dp[i] > maxviewtime:
                idx = i + 1
                maxviewtime = dp[i + adv_time] - dp[i]

    # print(maxviewtime,int_to_str(idx),int_to_str(idx + adv_time),dp[5:11])
    if idx == 1:
        answer = "00:00:00"
    else:
        answer = int_to_str(idx)
    return answer
