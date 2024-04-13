import sys
input = sys.stdin.readline
W,L,D = map(float,input().split())

rank = []
for w in range(21):
    for l in range(21):
        if 20-l-w>=0:
            rank.append([w,l,20-l-w])

import math
def nCr(n, r):
    return math.comb(n,r)

answer = [0,0,0,0,0]
for r in rank:
    w,l,d = r[0],r[1],r[2]
    probability = 1
    for _ in range(w):
        probability*=W
    for _ in range(l):
        probability*=L
    for _ in range(d):
        probability*=D
    cases = nCr(20,w) * nCr(20-w,l)
    probability*=cases
    
    score = 2000 + 50*w -50*l
    # print(r,score,cases,probability)
    if 1000<=score<=1499:
        answer[0] += probability
    elif 1500<=score<=1999:
        answer[1] += probability
    elif 2000<=score<=2499:
        answer[2] += probability
    elif 2500<=score<=2999:
        answer[3] += probability
    else:
        answer[4] += probability
for i in answer:
    print("{:.8f}".format(round(i,8)))
