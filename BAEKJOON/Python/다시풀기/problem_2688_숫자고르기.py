import sys
input = sys.stdin.readline
n = int(input())
datas = [int(input()) for _ in range(n)]


# 뭐지? 조합으로 풀면 시간초과 날거고...
# 흠;;;??
# 일단 윗줄과 아랫줄이 같으면 무조건 추가하고..?
# dfs에 뭔 사이클이어쩌고 하는데 왜케 어렵냐 나한텐.. 보고배낌

graph = {}
for i in range(1,n+1):
    graph[i] = []
for i,v in enumerate(datas):
    graph[v]+=[i+1]
# print(graph)

visited = [0]*(n+1)
answer = []
def dfs(cnode):
    routes.add(cnode)
    visited[cnode]=1
    for i in graph[cnode]:
        if i not in routes:
            dfs(i)
            routes.remove(i)
        else:
            # print(routes)
            answer.extend(routes)

for st in range(1,n+1):
    routes = set()
    if visited[st]==0:
        dfs(st)

# print(answer)
answer.sort()
print(len(answer))
for i in answer:
    print(i)