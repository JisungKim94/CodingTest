def solution(n, results):
    answer = 0
    info = {}
    ath = 0
    for r in results:
        ath = max(ath, r[0], r[1])
        if r[0] not in info:
            info[r[0]] = [[r[1]], []]
        else:
            info[r[0]][0].append(r[1])

        if r[1] not in info:
            info[r[1]] = [[], [r[0]]]
        else:
            info[r[1]][1].append(r[0])
    for i in info:
        info[i][0] = set(info[i][0])
        info[i][1] = set(info[i][1])
    print(info)

    for i in info:
        for w in info[i][0]:
            for giraffe in info[i][1]:
                info[w][1].add(giraffe)
        for l in info[i][1]:
            for giraffe in info[i][0]:
                info[l][0].add(giraffe)

    for i in info:
        if (len(info[i][0]) + len(info[i][1])) == ath - 1:
            answer += 1
    return answer
