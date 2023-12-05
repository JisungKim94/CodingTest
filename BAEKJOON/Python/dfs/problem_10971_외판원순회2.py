# N 이 작을때만 이렇게 풀 수 있음 

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# print(graph)

mincost = float("inf")
def dfs(start,cn,ccost,visited):
    global mincost
    if ccost>mincost:
        pass
    else:
        if (0 not in visited) and (graph[cn][start] != 0):
            mincost = min(mincost,ccost+graph[cn][start])
            # print(cn,mincost)
        else:
            for nn,cost in enumerate(graph[cn]):
                if visited[nn] == 0 and nn != start and cost!=0:
                    visited[nn] = 1
                    dfs(start,nn,ccost+cost,visited[:])
                    visited[nn] = 0

for start in range(N):
    visited = [0]*N
    visited[start] = 1
    dfs(start,start,0,visited)
    visited[start] = 0
print(mincost)