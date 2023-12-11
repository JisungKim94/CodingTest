N = int(input())
# characteristic value
cvalue = list(map(int,input().split()))
cvalue.sort()
# print(cvalue)

answer = 0
minval = 3000000001
for i in range(N-2):
    l,r = i+1,N-1
    while l<r:
        curval = (cvalue[i]+cvalue[l]+cvalue[r])
        if minval > abs(curval):
            minval = abs(curval)
            answer = [i,l,r]
        
        if curval<0:
            l+=1
        else:
            r-=1
    # print(minval,answer)    
    
print(cvalue[answer[0]],cvalue[answer[1]],cvalue[answer[2]])