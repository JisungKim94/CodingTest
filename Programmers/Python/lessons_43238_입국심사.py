def solution(n, times):
    answer = 0
    times.sort()
    # end 초기값 제일 늦은 곳에서 모두 심사 받을 때(최대값)
    start, end, mid = 1, times[-1] * n, 0

    while start < end:
        # 이분탐색
        mid = (start + end) // 2
        NumberOfPassedPeople = 0
        # mid//time 으로 한 심사관이 검사 할 수 있는 사람 수 구함
        # 한사람이 소수점이 될 수 없으니 // 사용 .xxx 는 내림 처리
        # 해야하므로 // 그대로 써도 됨
        for time in times:
            NumberOfPassedPeople = NumberOfPassedPeople + (mid // time)
        # 위에서 구한 사람 수가 n명을 넘으면 그 값이
        # 정답 후보가 됨, 다음 이분 탐색의 end로 사용
        # n명 이하면 그보단 커야 하므로 +1 해서 start로 사용
        if NumberOfPassedPeople >= n:
            end = mid
        else:
            start = mid + 1
    answer = end
    # 잘 짰으면 end == start 임
    # answer = start
    return answer
