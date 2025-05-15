def solution(lines):
    answer = 0
    times = [0] * 3600 * 24 * 1000
    for line in lines:
        line = line.split(" ")
        dr = float(line[-1][:-1]) * 1000
        line = line[1].split(":")
        hh, mm, ss = (
            float(line[0]) * 3600000,
            float(line[1]) * 60000,
            float(line[2]) * 1000,
        )
        done = int(hh + mm + ss)
        start = int(done - dr)

    answer = max(times)
    return answer
