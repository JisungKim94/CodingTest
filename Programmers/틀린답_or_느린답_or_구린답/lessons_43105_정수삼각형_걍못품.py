def DP(idx_, triangle_, cnt_, answer_, direction_):
    cnt_ = cnt_ - 1
    if cnt_ > -len(triangle_):
        if idx_ == 0:
            idx_upper_row = 0
            direction_.append("r")
        elif idx_ == len(triangle_[cnt_ - 1]):
            idx_upper_row = len(triangle_[cnt_ - 1]) - 1
            direction_.append("l")
        else:
            if triangle_[cnt_ - 1][idx_ - 1] > triangle_[cnt_ - 1][idx_]:
                idx_upper_row = idx_ - 1
                direction_.append("l")
            elif triangle_[cnt_ - 1][idx_ - 1] < triangle_[cnt_ - 1][idx_]:
                idx_upper_row = idx_
                direction_.append("r")
            else:
                if DP(idx_ - 1, triangle_, cnt_, answer_, direction_) > DP(
                    idx_, triangle_, cnt_, answer_, direction_
                ):
                    idx_upper_row = idx_ - 1
                    direction_.append("l")
                else:
                    idx_upper_row = idx_
                    direction_.append("r")

                direction_.append("l")
        answer_ = DP(idx_upper_row, triangle_, cnt_, answer_, direction_)
        answer_ = answer_ + triangle_[cnt_ - 1][idx_upper_row]
    return answer_


def solution(triangle):
    answer = 0
    direction = []
    answers = []
    cnt = 0

    for idx_, elm in enumerate(triangle[-1]):
        answer = DP(idx_, triangle, cnt, elm, direction)
        print(answer)
        answers.append(answer)
        print(direction)
        answer = 0
        direction = []

    return max(answers)


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
