from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

adj = {}
indegree = [0]*N
timecost = [0]*N
for i in range(N):
    adj[i] = []

for i in range(N):
    temp = list(map(int,input().split()))
    timecost[i] = temp[0]
    indegree[i] += len(temp)-2
    for idx in range(1,len(temp)):
        if temp[idx]==-1:
            break
        adj[temp[idx]-1] += [i]
# print(adj)
# print(indegree)
# print(timecost)

answer = [0]*N
que = deque([])
for i,v in enumerate(indegree):
    if v == 0:
        que.append(i)
        answer[i]=timecost[i]

while que:
    # print(answer)
    # print(indegree)
    cnode = que.popleft()
    for nnode in adj[cnode]:
        indegree[nnode]-=1
        answer[nnode] = max(answer[nnode],answer[cnode]+timecost[nnode])
        if indegree[nnode]==0:
            que.append(nnode)


for a in answer:
    print(a)
