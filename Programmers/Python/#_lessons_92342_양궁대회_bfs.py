from collections import deque


def bfs(n, apeach_info):
    res = []
    que = deque([(0, [0 for _ in range(11)])])
    max_gap = 0

    while que:
        target, lion_info = que.popleft()
        # 화살 다 쏜지 확인
        if sum(lion_info) == n:
            apeach_score, lion_score = 0, 0
            for i in range(11):
                # 둘 다 0이면 pass
                if not (apeach_info[i] == 0 and lion_info[i] == 0):
                    # 승리조건
                    if apeach_info[i] >= lion_info[i]:
                        apeach_score = apeach_score + (10 - i)
                    else:
                        lion_score = lion_score + (10 - i)
            # 라이언이 이긴 조건 중 최대 점수차이 retrun
            if lion_score > apeach_score:
                temp_gap = lion_score - apeach_score
                if max_gap > temp_gap:
                    continue
                if max_gap < temp_gap:
                    max_gap = temp_gap
                    res.clear()
                res.append(lion_info)
        # 화살 더 쏜 경우
        elif sum(lion_info) > n:
            continue
        # 이미 이겼는데 화살은 덜 쏜 경우
        # 0점에 남은거 난사
        elif target == 10:
            temp = lion_info.copy()
            temp[target] = n - sum(lion_info)
            que.append((-1, temp))
        # 정상 진행 중
        else:
            # 라이언이 어피치가 쏜 곳에 한발 더 쏴서 점수를 얻는 경우 temp
            temp = lion_info.copy()
            temp[target] = apeach_info[target] + 1
            que.append((target + 1, temp))
            # 라이언이 어피치가 쏜 곳을 포기하고 아예 안쏘는 경우
            temp2 = lion_info.copy()
            temp2[target] = 0
            que.append((target + 1, temp2))
    return res


def solution(n, info):

    answer = bfs(n, info)

    if not answer:
        answer = [-1]
    elif len(answer) == 1:
        answer = answer[0]
    else:
        # 맨 뒤에 넣은게 제일 뒤쪽에 몰려있는 거니까
        answer = answer[-1]

    return answer


print(
    solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]) == [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]
)
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1])
print(
    solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]) == [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]
)
print(
    solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]) == [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]
)
