N = int(input())
num = 0

for i in range(0,N,1):
    temp_array = list(map(int, input().split()))
    
    avg = (sum(temp_array)-temp_array[0]) / (len(temp_array)-1)

    for i in range(len(temp_array)):
        temp_array[i] = temp_array[i]/avg
        if (temp_array[i]>1):
            num = num + 1
    print(str("%.3f" %(100*num/(len(temp_array)-1)))+"%")
    num = 0
    avg = 0
    temp_array = []