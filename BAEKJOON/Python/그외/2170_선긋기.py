import sys
input = sys.stdin.readline
N = int(input())
answer = 0
dots = []
for _ in range(N):
    dots.append(tuple(map(int, input().split())))

# print(dots)
dots.sort()
# print(dots)
cnt = 0
cl,cr = dots[0][0],dots[0][1]
for ld,rd in dots:
    if cl<=ld<=cr:
        cr=max(cr,rd)
    else:
        # print(cl,cr)
        answer+=(cr-cl)
        cl,cr = ld,rd
answer += (cr-cl)
print(answer)