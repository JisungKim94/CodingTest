a,b = map(int, input().split())

if (a<0 & b<0):
    print(3)
elif (a<0 & b>0):
    print(2)
elif (a>0 & b<0):
    print(4)
else:
    print(1)