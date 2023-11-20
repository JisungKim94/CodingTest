#참고 C:\98_Git\CodingTest\Programmers\lessons_63062_징검다리건너기_이분탐색.py
# 이진탐색의 lower, upper와 일반적인 코드에 따라 찾는 index가 다르다.
# 일반적 방법은 구한 값을 바로 반환하고
# lower/upper bound는 원하는 값보다 처음으로 크거나 작은 값이 나오는 위치를 찾는 방법
# https://woongsios.tistory.com/131
# 일반적 방법 -> while l<=r, if target <= arr[mid]: l=m+1, else: r=m-1
# lower bound -> while l<r, if target <= arr[mid]: l=m+1, else: r=m
# upper bound -> while l<r, if target < arr[mid]: l=m+1, else: r=m

import sys
input = sys.stdin.readline
D, N, M = map(int, input().split())
stone = [int(input()) for _ in range(N)]
stone.sort()
l,r = 0,D
# print(stone)
answer = 0
while l<=r:
    m = (l+r)//2
    # print("lmr", l,m,r)
    cnt = 0
    last = 0
    tmpanswer = 1000000001
    for i in range(len(stone)):
        # delta가 특정값(m)을 넘는 애들을 찾기위해 last는 특정값을 넘을때만 갱신
        delta = stone[i] - last
        if delta >= m:
            tmpanswer = min(tmpanswer,delta)
            last = stone[i] 
        else:
            # 특정값(m)을 못 넘으면 cnt+=1
            cnt+=1
    # 탈출섬과의 거리도 확인해야 함
    tmpanswer = min(tmpanswer,D-last)
    
    # print("m, tmp",m,tmpanswer)
    # 특정값(m)이분탐색
    if cnt>M:
        r=m-1
    else:
        l=m+1
        # 이분탐색에서 아래로 내릴땐 최소값이 아니라는 말이니까 갱신하면 안됨
        answer = max(answer,tmpanswer)

print(answer)
