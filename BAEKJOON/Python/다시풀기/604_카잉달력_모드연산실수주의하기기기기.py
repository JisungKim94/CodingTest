import sys
input = sys.stdin.readline
T = int(input())

# 규칙은 금방 찾았는데 구현에서 생각보다 좀 헤맸다.
# (cnt-x)%M==0 이거랑 cnt%M==x 이게 그렇게 다를줄 몰랐다..
# 보통 후자로 표현하는데 문제에 따라서 전자로 표시하는게 구현하기 쉬워지기도 하는구나~ 잘 배워두자
# a=14
# b=7
# for cnt in range(100):
#     if ((cnt-a)%b==0) == (cnt%b==a):
#         pass
#     else:
#         print(cnt, ((cnt-a)%b==0) == (cnt%b==a))


import math
for _ in range(T):
    M,N,x,y = map(int, sys.stdin.readline().rstrip().split())
    flag = 0
    if M==x and N==y:
        print(math.lcm(M,N))
        continue
    
    cnt = x
    while cnt<math.lcm(M,N):
        if ((cnt-x)%M==0 and (cnt-y)%N==0):
            flag = 1
            # print(math.lcm(M,N),cnt%M,cnt%N)
            break
        cnt+=M

        
    if flag:
        print(cnt)
    else:
        print(-1)
    

    
        
    
# # print(cnt%M,cnt%N)
