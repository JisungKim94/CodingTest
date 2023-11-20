from collections import deque
import sys
input = sys.stdin.readline


for T in range(int(input())):
    N,K = map(int,input().split())
    dealy = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(N+1)]
    parents = [-1] + [0]*(N)
    for _ in range(K):
        a,b = map(int,input().split())
        graph[a].append(b)
        parents[b] += 1
    obj = int(input())

    # print(graph,parents)
    dp = [-1]*(N+1)
    todoList = deque()
    for i in range(1,N+1):
        if parents[i] == 0:
            todoList.append(i)
            dp[i] = dealy[i]

    # dp 진행을 시키는데 특정 조건(parents의 수)을 만족할 경우에만 진행 시킨다.
    # 위상정렬이라고 부르는듯..?
    while todoList:
        # print(todoList)
        cnode = todoList.popleft()
        for tonode in graph[cnode]:
            parents[tonode] -= 1
            dp[tonode] = max(dp[tonode], dp[cnode]+dealy[tonode])
            if parents[tonode] == 0:
                todoList.append(tonode)
        if parents[obj] == 0:
            break
    # print("TC",T,"done")
    print(dp[obj])
