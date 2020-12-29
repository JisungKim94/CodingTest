N = int(input())
sum = 0
i = 0

while (1):
    sum = i + sum
    if (i&0b1==1)&(N<=sum):
        print('{}/{}'.format((1+(sum-N)),(i-(sum-N))))
        break
    elif (i&0b1==0)&(N<=sum):
        print('{}/{}'.format((i-(sum-N)),(1+(sum-N))))
        break

    i = i + 1