Test_case = int(input())

for i in range(Test_case):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    
    distance = ((x1-x2)**2 + (y1-y2)**2)**(0.5)            # 두 중심 사이의 거리
    
    # ============================ 여기가 핵심 ============================
    R = [r1, r2, distance]
    R_max = max(R)
    R.remove(R_max)
    # ============================ 여기가 핵심 ============================

    if (distance == 0 & r1 == r2):
        ret = -1
    else:
        if ((distance == r1 + r2) | (R_max == sum(R))):
            ret = 1
        elif (R_max > sum(R)):
            ret = 0
        else:
            ret = 2
    
    print(ret, end = "\n")
