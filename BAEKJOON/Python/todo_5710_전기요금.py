import sys
input = sys.stdin.readline


# 수학문제인가?
# x : 상근이(항상 최소요금) y : 이웃

# 전기 사용량 공식
# def calcusage(price):
#     usage = 0
#     if price>5000000-30000-200:
#         usage = (price-(5000000-30000-200))//7 + 100 + 10000 + 1000000
#     if price>30000-200:
#         usage = (price-(30000-200))//5 + 100 + 10000
#     if price>200:
#         usage = (price-(200))//3 + 100
#     else:
#         usage = (price)//2
#     return usage
# 전기 요금 공식
def calcprice(usage):
    price = 0
    if usage>1000000:
        price = (usage-1000000)*7 + 4979900
        return price
    if usage>10000:
        price = (usage-10000)*5 + 29900
        return price
    if usage>100:
        price = (usage-100)*3 + 200
        return price
    price = (usage)*2
    return price
    

# A = calcprice(x+y)
# B = calcprice(y)-calcprice(x)
while 1:
    A,B = map(int,input().split())
    if (A,B) == (0,0):
        break
    l,r = 0,10000000000
    while l<=r:
        xplusy = (l+r)//2
        if calcprice(xplusy) == A:
            break
        else:
            if calcprice(xplusy) <= A:
                l=xplusy+1
            else:
                r=xplusy-1
    x = 0
    y = xplusy - x
    # print(calcprice(y))
    # print(x,y)
    l,r = 0,10000000000
    while l<=r:
        x = (l+r)//2
        y = xplusy - x
        if abs(calcprice(y)-calcprice(x)) == B:
            break
        else:
            if calcprice(y)-calcprice(x) >= B:
                l=x+1
            else:
                r=x-1
    # print(x,y)
    if x>y:
        print(calcprice(y))
    else:
        print(calcprice(x))
