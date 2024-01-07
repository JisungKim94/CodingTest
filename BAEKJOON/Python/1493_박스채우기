import sys
input = sys.stdin.readline

# 1) 박스에 넣을 수 있는 가장 큰 큐브를 넣음
# 2) 남은 크기 구하기
# 3) 남는 크기가 근데 경우의 수가 여러개가 나오는데 어카지?
# 3) 그 박스들에 넣을 수 있는 가장 큰 큐브를 넣는걸 반복?

L,W,H = map(int, input().split())
boxes = [(L,W,H)]

N = int(input())
cubes = [0]*N
for _ in range(N):
    i,cnt = map(int, input().split())
    cubes[i] = cnt

box = boxes.pop()
minbox = min(box)
for i in range(cubes,0,-1):
    if cubes[i]>0 and 2**i<=minbox:
        cubes[i]-=1
        