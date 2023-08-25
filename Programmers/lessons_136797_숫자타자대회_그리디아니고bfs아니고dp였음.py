# 아래처럼 풀면 cost가 동점일 경우 처리가 안된다.
# bfs로 풀면 10만개라 시간초과가 난다.
# dp로 접근 해 보ㅏ라
# https://howudong.tistory.com/333


def costcheck(dist_r, dist_c):
    cost = 0
    if dist_r == 0 and dist_c == 0:
        return 1
    while dist_r > 0 or dist_c > 0:
        if dist_r > 0 and dist_c > 0:
            cost += 3
            dist_r -= 1
            dist_c -= 1
        elif dist_r > 0:
            cost += 2
            dist_r -= 1
        elif dist_c > 0:
            cost += 2
            dist_c -= 1

    return cost


def lrcheck(n, finger_l, finger_r):
    rows = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]
    cols = [["1", "4", "7", "*"], ["2", "5", "8", "0"], ["3", "6", "9", "#"]]
    for i_row, r in enumerate(rows):
        if n in r:
            break
    for i_col, c in enumerate(cols):
        if n in c:
            break
    dist_lr, dist_lc = abs(finger_l[0] - int(i_row)), abs(finger_l[1] - int(i_col))
    dist_rr, dist_rc = abs(finger_r[0] - int(i_row)), abs(finger_r[1] - int(i_col))
    cost_l, cost_r = costcheck(dist_lr, dist_lc), costcheck(dist_rr, dist_rc)

    return cost_l, cost_r, i_row, i_col


def solution(numbers):
    answer = 0
    finger_l, finger_r = [1, 0], [1, 2]
    # print(finger_l,finger_r,answer)
    for i, n in enumerate(numbers):
        cost_l, cost_r, i_row, i_col = lrcheck(n, finger_l, finger_r)
        if cost_l > cost_r:
            finger_r[0], finger_r[1] = int(i_row), int(i_col)
            answer += cost_r
        elif cost_l < cost_r:
            finger_l[0], finger_l[1] = int(i_row), int(i_col)
            answer += cost_l
        else:
            temp_r = [int(i_row), int(i_col)]
            temp_l = [int(i_row), int(i_col)]
            if i + 1 < len(numbers):
                if (lrcheck(numbers[i + 1], finger_l, temp_r)) < (
                    lrcheck(numbers[i + 1], temp_l, finger_r)
                ):
                    finger_r[0], finger_r[1] = int(i_row), int(i_col)
                    answer += cost_r
                else:
                    finger_l[0], finger_l[1] = int(i_row), int(i_col)
                    answer += cost_l
            else:
                answer += cost_l
        # print(finger_l,finger_r,answer)
    return answer
