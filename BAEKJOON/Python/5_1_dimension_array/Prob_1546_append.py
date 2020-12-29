N = int(input())
array = list(map(int,input().split()))

Max = max(array)

New_array = []
avg = 0
for i in range(0, N, 1):
    New_array.append(array[i]/Max*100)
print("%.2f" %(sum(New_array)/len(New_array)))