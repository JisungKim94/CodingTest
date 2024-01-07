l = int(input())
r = int(input())
k = int(input())
answer = 0
if k==2:
    range_ = range(max(l,3),r+1)
    # 2k+d
    for r in range_:
        answer+=1
elif k==3:
    range_ = range(max(l,6),r+1)
    # 3k+3d
    for r in range_:
        if r%3==0:
            answer+=1
elif k==4:
    range_ = range(max(l,10),r+1)
    # 4k+6d = 2(2k+3d) = 2*(5(1,1),7(2,1),8(1,2),9(3,1),10(2,2),
    #                    11(1,3)...) 6은 못 만듬(12제외)
    for r in range_:
        if r%2==0 and r!=12:
            answer+=1
else:
    range_ = range(max(l,15),r+1)
    # 5k+10d = 5(k+2d)
    for r in range_:
        if r%5==0:
            answer+=1

print(answer)