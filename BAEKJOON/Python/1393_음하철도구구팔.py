import sys
import math
input = sys.stdin.readline
# 점과 직선사이의 거리로 풀라면 조건이 복잡해짐 직선이 아니고 벡터라 반대로는 못가는거 잡기가 귀찮음

xs, ys = map(int, input().split())
xe,ye,dx,dy = list(map(int, input().split()))
temp = math.gcd(dx, dy)
dx, dy = dx//temp, dy//temp
x, y = xe, ye
while ((x-xs)**2+(y-ys)**2) > ((x+dx-xs)**2+(y+dy-ys)**2):
    x += dx
    y += dy
print(x, y)
