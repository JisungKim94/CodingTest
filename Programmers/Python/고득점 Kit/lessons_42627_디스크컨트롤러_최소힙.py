# 쫌 애매한 문제
import heapq


def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    # 시작시간 초기화
    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                # 작업 소요시간으로 min heap을 만들기 위해 (t, s) 푸시
                heapq.heappush(heap, (t, s))
        # 바로 수행할 수 있는 작업이 있는 경우 이전시간은 현재시간이 되고
        # 현재 시간은 이전시간 + 소요시간이 된다.
        if len(heap) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(heap)
            time += term
            # 요청부터 종료까지 걸린 시간의 평균이 답이니까
            answer += time - start
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            time += 1
    return answer // len(jobs)


test_case = [[0, 5], [1, 2], [5, 5]]
print("solutions :", solution(test_case))
