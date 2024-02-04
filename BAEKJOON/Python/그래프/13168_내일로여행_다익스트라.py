import sys
input = sys.stdin.readline

# 최소유량으로 풀수 있는 문제같긴 한데..
# 다익스트라로도 되지않을까? 다익스트라로 해 봐야겠다 최소유량은 구현 할 자신이 없다.;
# 다익스트라로는 불가능하다.

N,R = map(int, input().split())
cities = list(map(str, input().split()))

M = int(input())
tourlist = list(map(str, input().split()))
K = int(input())
# print(cities)
transportation = {}
cityidx = {}
for i,v in enumerate(cities):
    transportation[v] = []
    cityidx[v] = i
# print(transportation)
# print(tourlist)
typeidx = {"Subway":0, "Bus":1, "Taxi":2, "Airplane":3, "KTX":4, "S-Train":5, "V-Train":6, "ITX-Saemaeul":7, "ITX-Cheongchun":8, "Mugunghwa":9}

for _ in range(K):
    Type,S,E,Cost = map(str, input().split())
    Cost = int(Cost)
    costs = [100001]*10
    costs[typeidx[Type]]=Cost
    transportation[S] += [(E,costs)]
    transportation[E] += [(S,costs)]
    # print(Type,S,E,Cost)
# print(transportation["Yeosu"])

import collections
import heapq
answer1 = 0
for i in range(len(tourlist)-1):
    que = []
    dist = [float('inf')]*len(cities)
    heapq.heappush(que,(0,tourlist[i]))
    while que:
        ccost,ccity = heapq.heappop(que)
        if dist[cityidx[ccity]]<ccost:
            continue
        
        for ncity,cost in transportation[ccity]:
            mincost = min(cost)
            if dist[cityidx[ncity]] > ccost + mincost:
                dist[cityidx[ncity]] = ccost + mincost
                heapq.heappush(que,(ccost + mincost,ncity))
    # print(tourlist[i],tourlist[i+1],dist[cityidx[tourlist[i+1]]])
    answer1 += dist[cityidx[tourlist[i+1]]]

naeilfree = [7,8,9]
naeil50off = [5,6]
def naeilmin(cost):
    mintemp = 100001
    for i in range(len(cost)):
        if cost[i] == 100001:
            continue
        if i in naeilfree:
            temp = 0
        elif i in naeil50off:
            temp = cost[i]/2
        else:
            temp = cost[i]
        mintemp = min(temp,mintemp)
    return mintemp

answer2 = R
for i in range(len(tourlist)-1):
    que = []
    dist = [float('inf')]*len(cities)
    heapq.heappush(que,(0,tourlist[i]))
    while que:
        ccost,ccity = heapq.heappop(que)
        if dist[cityidx[ccity]]<ccost:
            continue
        
        for ncity,cost in transportation[ccity]:
            mincost = naeilmin(cost)
            if dist[cityidx[ncity]] > ccost + mincost:
                dist[cityidx[ncity]] = ccost + mincost
                heapq.heappush(que,(ccost + mincost,ncity))
    # print(tourlist[i],tourlist[i+1],dist[cityidx[tourlist[i+1]]])
    answer2 += dist[cityidx[tourlist[i+1]]]
    if answer2>=answer1:
        break

# print(answer1,answer2)        
if answer2>=answer1:
    print("No")
else:
    print("Yes")
