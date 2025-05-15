def solution(clothes):
    from collections import Counter
    from functools import reduce

    # collections.Counter 사용법
    # https://excelsior-cjh.tistory.com/94
    cnt = Counter([kind for name, kind in clothes])
    # functools.reduce 사용법
    # 누적합을 해 주는 함수인데... reduce(func,list_,initial)
    # 아래 과정을 반복 함 (cnt = {'headgear': 2, 'eyewear': 1, 'ddd': 1})
    # x = func(initial,list_[0]) = e.g) x = 1 * (2 + 1)
    # x = func(x, list_[1]) = e.g) x = 3 * (1 + 1)
    # x = func(x, list_[2]) = e.g) x = 6 * (1 + 1)
    # ...
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    print(cnt)
    return answer


print(
    solution(
        [
            ["yellowhat", "headgear"],
            ["bluesunglasses", "eyewear"],
            ["green_turban", "headgear"],
            ["abc", "ddd"],
        ]
    )
)
