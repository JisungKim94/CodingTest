def solution(n, cores):
    answer = 0
    if n <= len(cores):
        return n

    remain_n = n - len(cores)

    # 해당 시간(lmr) 까지 처리한 작업 수 를 이분탐색
    l, r = 1, 100000000
    m = (l + r) // 2

    while l < r:
        complete = 0
        m = (l + r) // 2
        for c in cores:
            complete += m // c

        if complete >= remain_n:
            r = m
        else:
            l = m + 1

    for c in cores:
        remain_n -= (r - 1) // c

    # print("complete n",complete + len(cores), "l,m,r", l, m, r, "/", "remain n",remain_n)

    for idx, c in enumerate(cores):
        if r % c == 0:
            remain_n -= 1
        if remain_n == 0:
            break

    return idx + 1
