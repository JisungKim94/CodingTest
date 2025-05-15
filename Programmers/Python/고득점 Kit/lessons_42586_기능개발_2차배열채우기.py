progresses = [93, 30, 55]
# progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 30, 5]
# speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        # python에서 //는 몫 e.g) 70/30 = 2.xx 니까 몫은 2
        # +) %는 나머지 mod
        # print(((100 - p) // s))
        if len(Q) == 0 or Q[-1][0] < ((100 - p) // s):
            Q.append([((100 - p) // s), 1])
        else:
            Q[-1][1] += 1
    print(Q)
    # 존내 신기하게 쓰넴 list를 return 하는데 그 내부 값들을 이렇게 채울 수 있뜸 [Q[0][1], Q[1][1], Q[2][1]...]
    return [q[1] for q in Q]


solution(progresses, speeds)
