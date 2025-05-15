def solution(r1, r2):
    answer1 = 0
    y = r1
    for x in range(1, r1):
        while (x * x + y * y) >= (r1 * r1):
            y = y - 1
        answer1 = answer1 + y
    # print(answer1)
    answer1 = answer1 * 4 + (r1 - 1) * 4 + 1
    # print(answer1)

    y = r2
    answer2 = 0
    for x in range(1, r2):
        while (x * x + y * y) > (r2 * r2):
            y = y - 1
        answer2 = answer2 + y
    # print(answer2)
    answer2 = answer2 * 4 + r2 * 4 + 1
    # print(answer2)

    answer = answer2 - answer1
    return answer
