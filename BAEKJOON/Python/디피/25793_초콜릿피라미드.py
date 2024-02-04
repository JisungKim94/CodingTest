import sys
input = sys.stdin.readline
T = int(input())
dp1 = [0]*(10**6+1)
dp1[0] = 1
dp2 = [0]*(10**6+1)
for i in range(1,len(dp1)):
    dp1[i] = dp1[i-1] + (i**2 + (i+1)**2)
    dp2[i] = dp2[i-1] + (i*(i+1)*2)
# print(dp1[:5], dp2[:5])
for _ in range(T):
    R,C = map(int, input().split())
    minRC = min(R,C)
    white,black = 2*C*R*minRC -(C+R)*minRC**2 +dp1[minRC-1], 2*C*R*minRC -(C+R)*(minRC)**2 + dp2[minRC-1]
    print(white,black)

