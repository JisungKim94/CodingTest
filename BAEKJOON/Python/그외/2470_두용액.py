N = int(input())
arr = list(map(int, input().split()))
# print(arr)
arr.sort()
# print(arr)

l,r = 0,len(arr)-1
cur = float('inf')
answer = [0,0]
while l<r:
    summation = arr[l]+arr[r]
    if abs(cur)>abs(summation):
        cur = summation
        answer[0],answer[1] = arr[l],arr[r]
    else:
        pass
    
    if summation==0:
        break
    elif summation>0:
        r-=1
    else:
        l+=1
    
print(*answer)