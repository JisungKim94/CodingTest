import sys
input = sys.stdin.readline

# 최소유량으로 풀수 있는 문제같긴 한데..
# 다익스트라로도 되지않을까? 다익스트라로 해 봐야겠다 최소유량은 구현 할 자신이 없다.;
# 플로이드-워셜로 풀 수도 있음

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

# 플로이드-워셜
graph1 = [[[1000001 for _ in range(10)] for _ in range(len(cities) + 1)] for _ in range(len(cities) + 1)]
graph2 = [[[1000001 for _ in range(10)] for _ in range(len(cities) + 1)] for _ in range(len(cities) + 1)]
for _ in range(K):
    Type,S,E,Cost = map(str, input().split())
    Cost = int(Cost)
    graph1[cityidx[S]][cityidx[E]][typeidx[Type]]=Cost
    graph1[cityidx[E]][cityidx[S]][typeidx[Type]]=Cost
    graph2[cityidx[S]][cityidx[E]][typeidx[Type]]=Cost
    graph2[cityidx[E]][cityidx[S]][typeidx[Type]]=Cost

for i in range(len(graph1)):
    for j in range(len(graph1)):
        graph1[i][j] = min(graph1[i][j])

for k in range(len(cities)):
    for a in range(len(cities)):
        for b in range(len(cities)):
            graph1[a][b] = min(graph1[a][b], graph1[a][k] + graph1[k][b])
answer1 = 0
for i in range(len(tourlist)-1):
    answer1 += graph1[cityidx[tourlist[i]]][cityidx[tourlist[i+1]]]


naeilfree = [7,8,9]
naeil50off = [5,6]
def naeilmin(cost):
    mintemp = 1000001
    for i in range(len(cost)):
        if cost[i] == 1000001:
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
for i in range(len(graph2)):
    for j in range(len(graph2)):
        graph2[i][j] = naeilmin(graph2[i][j])

for k in range(len(cities)):
    for a in range(len(cities)):
        for b in range(len(cities)):
            graph2[a][b] = min(graph2[a][b], graph2[a][k] + graph2[k][b])
for i in range(len(tourlist)-1):
    answer2 += graph2[cityidx[tourlist[i]]][cityidx[tourlist[i+1]]]




# print(answer1,answer2)        
if answer2>=answer1:
    print("No")
else:
    print("Yes")