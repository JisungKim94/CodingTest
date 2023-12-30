N, M = map(int, input().split())
land = list(map(int, input().split()))
temp = [0]*(N+1)
# print(temp)
for _ in range(M):
    st,end,score = map(int, input().split())
    temp[st-1]+=score
    temp[end]-=score
    # print(temp)
for i in range(1,N):
    temp[i]=temp[i-1]+temp[i]
# print(temp)

for i in range(N):
    land[i]=land[i]+temp[i]
for i in land:
    print(i, end=' ')