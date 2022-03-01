import math


def solution(w, h):
    answer = -1
    gcd_ = math.gcd(w, h)
    w_ = w / gcd_
    h_ = h / gcd_
    # print(w_, h_)
    # print(w_ + h_ - 1)
    # print(w / w_, h / h_)
    answer = w * h - ((w_ + h_ - 1) * (w / w_))

    return answer


print(solution(8, 12) == 80)
