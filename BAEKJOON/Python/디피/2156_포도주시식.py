N = int(input())
cups = [int(input()) for _ in range(N)]
dp = [[] for _ in range(N)]
dp[0]= [(0,0),(1,cups[0])]
answer = 0

for i in range(1,N):
    for dp_ in dp[i-1]:
        if dp_[0]==0:
            dp[i].append((1,dp_[1]+cups[i]))
            temp0 = (0,dp_[1])
        elif dp_[0]==1:
            dp[i].append((2,dp_[1]+cups[i]))
            temp1 = (0,dp_[1])
        else:
            temp2 = (0,dp_[1])
    if i == 1:
        if temp0[1]>temp1[1]:
            dp[i].append(temp0)
        else:
            dp[i].append(temp1)
        continue
    
    # 2개 연속으로 안 고르는 case를 생각을 못 했었고 아래 3개 max 찾는 코드 구현을 좀 애먹었었다.
    temp = (max([temp0,temp1,temp2],key=lambda x: x[1]))
    dp[i].append(temp)
    
for j in dp[-1]:
    answer = max(answer,j[1])
print(answer)