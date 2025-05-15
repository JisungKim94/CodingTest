import copy
import collections
import sys
input = sys.stdin.readline
N = int(input())
loc = list(map(int,input().split()))
T = int(input())
loc.sort()
dir = [-1,1]
giraffe = []
def dfs(idx,d,temp):
    if idx == len(loc):
        giraffe.append(temp)
        return
    for d in dir:
        temp.append([loc[idx],d])
        dfs(idx+1,d,copy.deepcopy(temp))
        temp.pop()
temp = collections.deque([])    

dfs(0,0,temp)
answer = 0
for idx in range(len(giraffe)):
    g = giraffe[idx]
    Time = T
    tempanswer = 0
    # print(g)
    while g and Time>=0:
        while g and g[0][1] == -1:
            g.popleft()
        while g and g[-1][1] == 1:
            g.pop()
        if len(g) == 0:
            continue
        collisionTime = 100000001
        for i in range(len(g)):
            if i < len(g)-1 and (g[i][1] == 1 and g[i+1][1]==-1) and (g[i+1][0] - g[i][0])/2 <= Time:
                mean = (g[i+1][0] - g[i][0])/2
                collisionTime = min(collisionTime, mean)
        Time-=collisionTime
        for i in range(len(g)):
            g[i][0] += g[i][1]*collisionTime
            if i<len(g) and g[i-1][0] == g[i][0]:
                g[i-1][1],g[i][1] = -g[i-1][1],-g[i][1]
                tempanswer += 1
    answer += tempanswer

print(answer/(2**N))