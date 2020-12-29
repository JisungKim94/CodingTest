num = int(input())

if (num < 10):
    num = 10

result = num
cnt = 0
sumnum = 0

while (1):
    firstnum = (int)(result/10)
    secondnum = result%10
    sumnum = firstnum + secondnum
    result = (secondnum*10) + (sumnum %10)
    cnt = cnt + 1
    
    if (num == result):
        break

print(cnt)