import sys
input = sys.stdin.readline

N = int(input())
potions = []
for _ in range(N):
    potions.append(int(input()))
# print(potions)

# 투포인터고 홀수번째인지 짝수번째인지에 따라서 증가하는 구간의 끝 감소하는 구간의 끝으로 판단

#71836
cnt = 0
l,r = 0,0
preval = 0
answer = 0
while r<len(potions):
    # print(answer,preval,potions[r])
    if cnt%2 == 0:
        if preval <= potions[r]:
            preval=potions[r]
            r+=1
        else:
            answer+=preval
            preval=potions[r]
            r+=1
            cnt+=1
    else:
        if preval >= potions[r]:
            preval=potions[r]
            r+=1
        else:
            answer-=preval
            preval=potions[r]
            r+=1
            cnt+=1

if cnt%2==0:
    answer+=preval
print(answer)