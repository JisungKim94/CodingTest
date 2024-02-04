import sys
input = sys.stdin.readline

import itertools

N = int(input())
balls = list(map(int, input().split()))
answer = 0

while len(balls)>2:
    idx = 0
    maxenergy = 0
    for i in range(1,len(balls)-1):
        if maxenergy<balls[i-1]*balls[i+1]:
            maxenergy = balls[i-1]*balls[i+1]
            idx = i
    balls.pop(idx)
    print(idx)
    answer += maxenergy
print(answer)