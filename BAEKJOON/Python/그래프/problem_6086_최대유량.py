# 네트워크 흐름이라는 문제 유형이며
# 에드몬드-카프 알고리즘으로 풀 수있다고 함. 더 어려운건 다닉? 디닉? 으로 풀어야한다고 함
# 동일한 유형으로 이분매칭(남여짝 매칭) 문제가 있다고 함..

# 원래 a~z A~Z 총 52개노드 해야되는데 알고리즘 이해가 안되서 일단 G까지로 줄여놨음 이해하고 다시 Z로 바꾸자
# 이해좀 해보자 아따 어렵다;;


import sys
input = sys.stdin.readline
N = int(input())
pipes = []
# 'A'~'Z' => 0~25, 'a'~'z' => 26~51
h = lambda x: ord(x) - ord('A') if x <= 'Z' else ord(x) - ord('a') + 26
for _ in range(N):
    temp = list(map(str, input().split()))
    temp[0],temp[1],temp[2] = h(temp[0]),h(temp[1]),int(temp[2])
    pipes.append(temp)
# print(pipes)

# Flow,Capacity,Source,Sink,adj
giraffe = 7 # temp G is sink
capacity = [[0]*giraffe for _ in range(giraffe)]
flow = [[0]*giraffe for _ in range(giraffe)]
adj = [[] for _ in range(giraffe)]
source = 0 # 'A'
sink = 6 # 'Z' temp G is sink

# 동일한 노드 입력이 여러번 있다고 함.. 문제 나쁘다..
for u,v,c in pipes:
    capacity[u][v] += c
    capacity[v][u] += c
    adj[u].append(v)
    adj[v].append(u)

def make_flow(path):
    c = 10e9
    cur = sink
    while cur != source:
        c = min(c, capacity[path[cur]][cur]-flow[path[cur]][cur])
        cur = path[cur]
    cur = sink
    while cur != source:
        flow[path[cur]][cur] += c
        flow[cur][path[cur]] -= c
        cur = path[cur]
    return c
    

# stack, pop구조가 아니고 que를 계속 첨부터 돌려주는 bfs..
def bfs():
    path = [-1]*giraffe
    stack = [source]
    for u in stack:
        for v in adj[u]:
            if capacity[u][v] - flow[u][v] > 0 and path[v] == -1:
                stack.append(v)
                path[v] = u
                if v == sink:
                    c = make_flow(path)
                    return c
    return 0

maxflow = 0
while 1:
    c = bfs()
    if c>0:
        maxflow+=c
    else:
        break
print(maxflow)