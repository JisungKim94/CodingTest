def mehaton_dis(loc1, loc2, locO):
    ret = 1
    if (abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])) > 2:
        ret = 1
    else:
        # print(range(min(loc1[0], loc2[0]), max(loc1[0], loc2[0])))
        # print(range(min(loc1[1], loc2[1]), max(loc1[1], loc2[1])))
        # print(loc1[0], loc2[0], loc1[1], loc2[1])
        # print(range(min(loc1[0], loc2[0]), max(loc1[0], loc2[0])))
        # print(range(min(loc1[1], loc2[1]), max(loc1[1], loc2[1])))
        for i in range(min(loc1[0], loc2[0]), max(loc1[0], loc2[0]) + 1):
            for j in range(min(loc1[1], loc2[1]), max(loc1[1], loc2[1]) + 1):
                if (
                    len(range(min(loc1[1], loc2[1]), max(loc1[1], loc2[1])))
                    + len(range(min(loc1[0], loc2[0]), max(loc1[0], loc2[0])))
                    < 2
                ):
                    ret = 0
                if [i, j] in locO:
                    ret = 0
    return ret


def solution(places):
    answer = []
    temp_answer = 0
    row = 0
    column = 0
    locP = []
    locO = []
    cnt = 1

    for i in places:
        for j in i:
            row = row + 1
            for k in j:
                column = column + 1
                # print(row, column)
                if k == "P":
                    locP.append([row - 1, column - 1])
                elif k == "O":
                    locO.append([row - 1, column - 1])
            column = 0
        row = 0
        # print(locP)
        temp_answer = 1
        for idx1 in range(len(locP)):
            for idx2 in range(len(locP)):
                if idx1 == idx2:
                    continue
                if (mehaton_dis(locP[idx1], locP[idx2], locO)) == 0:
                    temp_answer = 0
                    # break

        answer.append(temp_answer)

        locP = []
        locO = []
        cnt = cnt + 1
    print(answer)
    return answer


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXXX", "OOXOP", "POXXP"],
            ["OOOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPO"],
            ["PXOPX", "OXOXP", "OXOOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
    == [1, 0, 1, 1, 1]
)
