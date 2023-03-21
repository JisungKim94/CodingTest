def solution(dirs):
    answer = 0
    ways = []
    x_cur, y_cur = 0, 0
    x_pre, y_pre = 0, 0
    for i in dirs:
        x_pre = x_cur
        y_pre = y_cur
        if (i == "U") & (y_cur < 5):
            y_cur = y_cur + 1
            temp1 = ((x_pre, y_pre), (x_cur, y_cur))
            temp2 = ((x_cur, y_cur), (x_pre, y_pre))
            if (temp1 not in ways) & (temp2 not in ways):
                ways.append(temp1)
                ways.append(temp2)
        elif (i == "L") & (x_cur > -5):
            x_cur = x_cur - 1
            temp1 = ((x_pre, y_pre), (x_cur, y_cur))
            temp2 = ((x_cur, y_cur), (x_pre, y_pre))
            if (temp1 not in ways) & (temp2 not in ways):
                ways.append(temp1)
                ways.append(temp2)
        elif (i == "D") & (y_cur > -5):
            y_cur = y_cur - 1
            temp1 = ((x_pre, y_pre), (x_cur, y_cur))
            temp2 = ((x_cur, y_cur), (x_pre, y_pre))
            if (temp1 not in ways) & (temp2 not in ways):
                ways.append(temp1)
                ways.append(temp2)
        elif (i == "R") & (x_cur < 5):
            x_cur = x_cur + 1
            temp1 = ((x_pre, y_pre), (x_cur, y_cur))
            temp2 = ((x_cur, y_cur), (x_pre, y_pre))
            if (temp1 not in ways) & (temp2 not in ways):
                ways.append(temp1)
                ways.append(temp2)

    answer = len(ways) / 2
    return answer


print(solution("ULURRDLLU") == 7)
print(solution("LULLLLLLU") == 7)
print(solution("LURDLURDLURDLURD") == 4)
