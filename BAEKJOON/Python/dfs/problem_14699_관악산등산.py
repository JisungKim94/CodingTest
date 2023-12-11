import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rests = list(map(int, input().split()))
newrests = []
for i,v in enumerate(rests):
    newrests.append((v,i))
dic = {} # 높이,연결된 쉼터
for i in range(len(newrests)):
    dic[i+1] = [newrests[i][0],[]]
for i in range(M):
    u, v = map(int, input().split())
    if dic[u][0] < dic[v][0]:
        dic[u][1].append(v)
    if dic[v][0] < dic[u][0]:
        dic[v][1].append(u)
# print(dic)
newrests.sort(reverse=1)
# print(newrests)
visited = [0]*N
answer = []
def dfs(ccost,cnode):
    global maxcost
    maxcost = max(maxcost,ccost)
    if visited[cnode-1] != 0:
        ccost = ccost + visited[cnode-1] - 1
        maxcost = max(maxcost,ccost)
        visited[i] = maxcost
    else:
        if dic[cnode][1]:
            for nnode in dic[cnode][1]:
                dfs(ccost+1,nnode)
        else:
            maxcost = max(maxcost,ccost)
            visited[i] = maxcost

for h,i in newrests:
    maxcost = 0
    dfs(1,i+1)
    answer.append((i,maxcost))
# print(answer)
answer.sort()
for i,a in answer:
    print(a)
