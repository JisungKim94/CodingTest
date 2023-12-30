import sys
input = sys.stdin.readline
N,M = map(int, input().split()) # 학생들 번호, 비교한 수
comp = [tuple(map(int, input().split())) for _ in range(M)]

# 이거 권투 순위 정하는 프로그래머스 문제랑 같은거네...
# 근데 어캐 풀었는지 기억이 잘 안난다...
# 일단 걍 무식하게 앞뒤 추가로 해봤음 -> 시간초과
#
# import collections
# stack = collections.deque([])
# def notin(a,b,stack):
#     for i,v in enumerate(stack):
#         if a == v:
#             return False,(i,b)
#         elif b == v:
#             return False,(i,a)
#     return True,(0,0)
# for a,b in comp:
#     # print(stack,a,b)
#     flag,(idx,value) = notin(a,b,stack)
#     if flag:
#         stack.appendleft(a)
#         stack.append(b)
#     else:
#         if value==a:
#             stack.insert(idx,value)
#         else:
#             stack.insert(idx+1,value)
# print(*stack)
# 
# 이번엔 dict로 풀어보자 [[나보다앞],[나보다뒤]] ... 모루겠다 안된다 잘
# 아 모르겠어서 알고리즘 분류 봤음 그래프이론 위상정렬이라네..
# 위상정렬 알고리즘 검색해서 적용 해 봤음 위상정렬은 그런거라고 보면 된다.
# 우리 SW인증시험에서 일정 계산할 때 C 작업 하려면 선행 작업으로 A,B 있고 뭐 이런 문제 푸는거라고 보면 된다.
# 이걸 만족하는 순서를 정하는거임

from collections import deque

graph = {}
indegree = [0]*(N+1)
for i in range(1,N+1):
    graph[i] = []
for a,b in comp:
    graph[a] += [b]
    indegree[b] += 1
# print(indegree)
    

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복, 만약 n개 방문 전에 q가 빈다면 사이클이 있다는 뜻
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # cycle 발생 판단 하는 법, n번 도는동안 q가 비는지 확인
    # for _ in range(N):
    #   if len(q)==0:
    #       print('cycle 발생')
    #     # 큐에서 원소 꺼내기
    #     now = q.popleft()
    #     result.append(now)
    #     # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    #     for i in graph[now]:
    #         indegree[i] -= 1
    #         # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
    #         if indegree[i] == 0:
    #             q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()