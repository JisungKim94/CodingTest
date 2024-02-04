import sys
from collections import deque
import itertools

input = sys.stdin.readline
N = int(input())
info = list(map(int, input().split()))

# 뭐 모르고 풀었는데 이런 방식을 브루트포스(백트래킹) 이라고 한다고 함
# https://hcr3066.tistory.com/27

marbles = info[::]
answer = 0

def dfs(marbles,i,tempanswer,temp):
    global answer
    # print(i,marbles,tempanswer,temp)
    tempanswer += marbles[i-1]*marbles[i+1]
    temp.append((i,marbles.pop(i)))
    
    if len(marbles)>2:
        for idx in range(1,len(marbles)-1):
            dfs(marbles,idx,tempanswer,temp)
            t = temp.pop()
            marbles.insert(t[0],t[1])
    else:
        answer=max(answer,tempanswer)
    


for i in range(1,len(marbles)-1):
    marbles = info[::]
    dfs(marbles,i,0,[])
print(answer)