# 바로 답을 맞추는게 아니라 시간을 특정해서 그 시간이 답인지 확인 해 나가는 방식
# 이 때 이분탐색을 이용하는 문제임
def solution(n, times):
    answer = 0
    start, end, mid = 1, times[-1] * n, 0

    while start < end:
        mid = (start + end) // 2
        total = 0
        for time in times:
            total += mid // time

        if total >= n:
            end = mid
        else:
            start = mid + 1
    answer = start
    return answer


print(solution(6, [7, 11, 13]))
