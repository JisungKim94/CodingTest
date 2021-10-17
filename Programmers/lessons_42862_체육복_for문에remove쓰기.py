# n = 5
# lost = [2, 4]
# reserve = [1, 3, 5]
# n = 1
# lost = [1]
# reserve = [1]
n = 3
lost = [1, 2, 3]
reserve = [1, 2, 3]
# n = 5
# lost = [2, 3, 4]
# reserve = [3, 4, 5]
# n = 4
# lost = [2, 3]
# reserve = [3, 4]
n = 5
lost = [1, 3, 5]
reserve = [2, 3, 6]
# n = 3
# lost = [1, 2]
# reserve = [2, 3]
# n = 4
# lost = [4, 2]
# reserve = [3, 5]
# n = 5
# lost = [1, 2]
# reserve = [2, 3]
# n = 5
# lost = [5, 4, 2]
# reserve = [2, 4]


def solution(n, lost, reserve):
    answer = 0
    # 1. 여벌 체육복이 있는데 도난당한 경우 제외
    # 2. reserver list를 for문의 조건으로 사용하기 때문에
    # 내부에서 remove 하면 for문 조건이 달라지기 때문에 오류가 발생
    # 따라서 아래와 같은 code를 사용해야 한다.
    # 아래와 같은 code를 사용하면, reserve[:]로 list를 복사해서
    # 사용하기 때문에 for문 조건으로 사용하는 r이 오류없이 돌아감
    for r in reserve[:]:
        if r in lost:
            reserve.remove(r)
            lost.remove(r)

    for l in lost[:]:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            lost.remove(l)
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            lost.remove(l)
    answer = n - len(lost)
    return answer


print(solution(n, lost, reserve))
