def solution(k, ranges):
    answer = []
    Collatz = []
    Collatz.append(k)
    while k > 1:
        if k % 2 == 0:
            k = k / 2
        else:
            k = k * 3 + 1
        Collatz.append(k)

    tmp = 0
    tempanswer = 0
    s = 0
    e = 0
    for range_ in ranges:
        tempanswer = 0
        if abs(range_[0]) == 0 and abs(range_[1]) == 0:
            for i, v in enumerate(Collatz):
                if i == len(Collatz) - 1:
                    pass
                else:
                    tmp = Collatz[i + 1] * 1 - ((Collatz[i + 1] - Collatz[i]) / 2)
                    tempanswer = tempanswer + tmp
                    # print(tmp)
        elif abs(range_[0]) > (len(Collatz) - abs(range_[1]) - 1):
            tempanswer = -1.0
        else:
            s = range_[0]
            e = range_[1]
            for i in range(s, len(Collatz) + e - 1, 1):
                if i == len(Collatz) - 1:
                    pass
                else:
                    tmp = Collatz[i + 1] * 1 - ((Collatz[i + 1] - Collatz[i]) / 2)
                    tempanswer = tempanswer + tmp
        answer.append(tempanswer)
    return answer


print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]) == [33.0, 31.5, 0.0, -1.0])
