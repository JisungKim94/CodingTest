import sys
import math
input = sys.stdin.readline
N = int(input())

# 고민 끝에 나라에서는 각 사람들까지의 거리의 합이 최소가 되는 위치에 우체국을 세우기로 결정하였다. 우체국을 세울 위치를 구하는 프로그램을 작성하시오.
# 우체국 사이의 거리가 최소인거에 가중치만 넣어주면 될 것 같기도.. 안되네.. 이분탐색 해야할거같음 뭔가 느낌이
# 이거 뭔가 그 원숭이 나무 문제랑 비슷한거같음~! 아니면 입국탐색처럼 가야되려나?
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
# 일단 정답 확인용 코드
# mindist = float('inf')
# for i in range(arr[-1][0]+1):
#     dist = 0
#     peoples = 0
#     for j in range(N):
#         dist += abs(i-arr[j][0])*arr[j][1]
#         peoples += arr[j][1]
#     # print(i,dist)
#     if dist<mindist:
#         answer = i
#         mindist = dist
# print(answer)

# 왼쪽 오른쪽 다 가 보고 맞는쪽으로만 진행하는 방식?
l,r = arr[0][0],arr[-1][0]
m = (l+r)//2
while l<=r:
    # print(l,m,r)   
    m = (l+r)//2
    lm = (l+m)//2
    distm = 0
    for j in range(N):
        distm += abs(m-arr[j][0])*arr[j][1]
    distlm = 0
    for j in range(N):
        distlm += abs(lm-arr[j][0])*arr[j][1]
    rm = (r+m+1)//2
    distrm = 0
    for j in range(N):
        distrm += abs(rm-arr[j][0])*arr[j][1]
    # print(lm,m,rm)   
    # print(distlm,distm,distrm)
    if distm<distlm and distm<distrm:
        if distlm<=distrm:
            r = rm-1
        else:
            l = lm+1
    else:
        if distlm<=distrm:
            r = rm-1
        else:
            l = lm+1
print(m)