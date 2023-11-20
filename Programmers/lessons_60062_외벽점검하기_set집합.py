# dfs 풀이 시간초과
# dfs 풀이 시간초과
# dfs 풀이 시간초과
# import copy


# def checkallweak(weak, visited):
#     for w in weak:
#         if w not in visited:
#             return False
#     return True


# def solution(n, weak, dist):
#     answer = 0
#     dist.sort()
#     friends = len(dist)
#     visited = set([])
#     answer = []

#     def dfs(node, visited, dist, answer):
#         if checkallweak(weak, visited) or len(dist) == 0:
#             if checkallweak(weak, visited):
#                 # print(friends - len(dist))
#                 answer.append(friends - len(dist))
#             return answer

#         dist_ = copy.deepcopy(dist)
#         d = dist_.pop()
#         for w in weak:
#             if w in visited:
#                 continue
#             visited_ = copy.deepcopy(visited)
#             for i in range(w, d + w + 1):
#                 visited_.add(i % n)
#             answer = dfs(w, visited_, dist_, answer)
#         return answer

#     answer = dfs(weak[0], visited, dist, answer)
#     if answer:
#         return min(answer)
#     else:
#         return -1

# dfs 풀이 시간초과
# dfs 풀이 시간초과
# dfs 풀이 시간초과

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
    # 제일 많이 수리할 수 있는 애부터 제일 많이 수리할 수 있게 채워가다가
    # 다 수리하는 순간이 오면 그때가 최소 친구 투입
    for d in dist:
        answers = []
        count += 1
        # 제일 많이 수리하는 친구가 어디서부터 시작하는게 제일 많이 수리할 수 있는지 모르니까 다 해볼거임
        for i, start in enumerate(weak):
            ends = weak[i:]
            tmpans = []
            # n을 넘어가는 끝 값 후보들을 새로 만듬
            for w in weak[:i]:
                ends = ends + [n + w]
            # 지금 친구가 고칠 수 있는 지점 저장
            for end in ends:
                if end - start <= d:
                    tmpans = tmpans + [end % n]
            answers.append(set(tmpans))

        # 수리 가능한 경우
        cand = set()
        # 새 친구가 수리 가능지점을 기존 지점과 전체 비교
        for a in answers:  # 새친구의 수리가능 지점
            for x in repair_lst:  # 기존 수리가능 지점
                new = a | set(x)  # 새로운 수리가능 지점
                # new는 수리 가능한 케이스 전부 튜플 형태로 들어감
                if len(new) == W:  # 모두 수리가능 한 경우 친구 수 리턴
                    return count
                cand.add(tuple(new))
        repair_lst = cand

    return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]) == 2)
