N = int(input())
case = list(map(int, input().split()))
case_rev = case[::-1]
dp1 = [1]*N
dp2 = [1]*N

for i in range(N):
    for j in range(i,N):
        if case[i] < case[j]:
            dp1[j] = max(dp1[i]+1, dp1[j])
        if case_rev[i] < case_rev[j]:
            dp2[j] = max(dp2[i]+1, dp2[j])
        print(dp1)
    print("i번째 애는 j번째 애를 더하면 최대 위에만큼 길어질 수 있음","\n")

print(dp1,dp2)

temp = [0]*N
for i in range(N):
    temp[i] = dp1[i] + dp2[N-i-1] -1
print(max(temp))

# max index를 구하는 방법은 안통한다.. 왜냐?
# 감소하는걸 max로 둘지 증가하는걸 max로 둘지 다 안돌려보면
# 판단이 안되기 때문에 아래는 실패했던 코드
# print(dp1.index(max(dp1)))
# print(dp1,dp2[:(N-dp1.index(max(dp1))-1)])
# if max(dp1) >= max(dp2):
#     print( max(dp1) + max(dp2[:(N-dp1.index(max(dp1))-1)]) )
# else:
#     print( max(dp2) + max(dp1[:(N-dp2.index(max(dp2))-1)]) )

