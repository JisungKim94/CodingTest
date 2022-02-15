# 쫌 애매한 문제
import heapq


def solution(jobs):
    answer = 0
    # 소요시간 우선 정렬
    jobs = sorted(jobs, key=lambda x: x[1])
    length_jobs = len(jobs)
    task = []
    heap_ = []
    time_cur = 0
    time_proc = 0
    time_wait = 0
    cnt = 0
    is_end = False
    time_cur_pre = 0

    # jobs list 길이 만큼 반복
    while is_end == False:
        time_cur = time_cur_pre
        # jobs list에 있는 애들 하나씩 몽땅 비교
        for i, job in enumerate(jobs):
            # 현재 실행 가능한 작업 판단(요청시간이 현재 시간 내에 있는지)
            if time_cur >= job[0]:
                time_proc = job[1]
                time_wait = time_cur - job[0]
                time_cur = time_cur + time_proc
                # jobs list에 있는 애들 중 현재 실행 가능한 애들의 요청부터 종료까지
                # 걸린 시간과 인덱스를 최소힙에 집어넣음,
                heapq.heappush(heap_, (time_proc + time_wait, i))
            time_cur = time_cur_pre
            time_proc = 0
            time_wait = 0
        # 최소 힙에서 요청~종료 시간이 가장 짧은 애를 뽑음
        print("heap_ : ", heap_)
        if heap_:
            (time, idx) = heapq.heappop(heap_)
            time_proc = jobs[idx][1]
            time_wait = time_cur - jobs[idx][0]
            # 뽑은 애로 지나간 시간 연산
            time_cur_pre = time_cur + time_proc
            task.append(time)
            jobs.pop(idx)
            cnt = cnt + 1
            heap_ = []
        else:
            time_cur = time_cur + 1
            time_cur_pre = time_cur + time_proc

        if cnt == length_jobs:
            is_end = True
            answer = sum(task) // len(task)
            print(task)
    return answer


test_case = [
    [24, 10],
    [28, 39],
    [43, 20],
    [37, 5],
    [47, 22],
    [20, 47],
    [15, 2],
    [15, 34],
    [35, 43],
    [26, 1],
]
test_case = [[0, 5], [1, 2], [5, 5]]
# 정답 = 6
# 이 케이스가 중요함...
# 순간의 최소가 항상 전체의 최소는 아님
# 즉 위 알고리즘은 폐기해야댐
# 아래꺼나 공부 해 보자
# import heapq


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
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(heap) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(heap)
            time += term
            answer += time - start
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            time += 1
    return answer // len(jobs)


test_case = [[0, 5], [1, 2], [5, 5]]
print("solutions :", solution(test_case))
