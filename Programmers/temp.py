# tase case 놓침
# n = 200
# weak[] = [0, 10, 50, 80, 120, 160]
# dist[] = [1, 10, 5, 40, 30]
# return = 3
# maxcnt는 똑같이 2개씩인데 사용해야 하는 순서가 정해져있음

# !! 집합에 집합을 넣을 수 없으므로 tuple로 변경함
# !! 초기화를 set이 아니고 [()]로 하는 이유는 new = a | set(x)의 초기값이 공집합과의 합집합이 적용 되어야하기 때문
def solution(n, weak, dist):
    W, F = len(weak), len(dist)
    dist.sort(reverse=1)
    repair_lst = [()]
    count = 0  # 투입 친구 수
    for d in dist:
        answers = []
        repairs = []
        count += 1
        for i, start in enumerate(weak):
            ends = weak[i:]
            tmpans = []
            # 끝 값 새로 만듬
            for w in weak[:i]:
                ends = ends + [n + w]
            # 정답 후보들
            can = [end % n for end in ends if end - start <= d]  # 가능한 지점 저장
            repairs.append(set(can))
            for end in ends:
                if end - start <= d:
                    tmpans = tmpans + [end % n]
            print(tmpans, can)
            answers.append(set(tmpans))

        # 수리 가능한 경우
        cand = set()
        # 새친구 수리 가능지점을 기존 지점과 전체 비교
        for a in answers:  # 새친구의 수리가능 지점
            for x in repair_lst:  # 기존 수리가능 지점
                new = a | set(x)  # 새로운 수리가능 지점
                # new는 수리 가능한 케이스 전부 튜플 형태로 들어감
                if len(new) == W:  # 모두 수리가능 한 경우 친구 수 리턴
                    return count
                cand.add(tuple(new))
        repair_lst = cand

    return -1


print(solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]) == 3)
