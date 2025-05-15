#10:17
import sys
input = sys.stdin.readline
N = int(input())
ggul = list(map(int,input().split()))
prefix = [0]*(N)
prefix[0] = ggul[0]
for i in range(1,N):
    prefix[i]=prefix[i-1]+ggul[i]
# print(ggul)
# print(prefix)
# 벌이 한쪽에 두 개 있는 경우는 통이 끝에만 존재할 수 있고 벌 하나는 반대쪽 끝에만 존재할 수 있다.
# 벌이 양쪽에 두 개 있는 경우는 벌이 끝에만 존재할 수 있다.
answer = 0
# case1 통이 왼쪽 끝
tong = 0
for bul1 in range(1,N-1):
    # print("벌1,벌2,합",prefix[bul1-1]-0, prefix[-1]-ggul[-1]-ggul[bul1-1],(prefix[bul1-1]-0+prefix[-1]-ggul[-1]-ggul[bul1]))
    answer = max(answer,prefix[bul1-1]-0+prefix[-1]-ggul[-1]-ggul[bul1])
# case2 통이 오른쪽 끝
tong = N-1
for bul2 in range(1,N-1):
    # print("벌1,벌2,합",prefix[tong]-ggul[bul2]-ggul[0],prefix[tong]-prefix[bul2],(prefix[tong]-ggul[bul2]-ggul[0]+prefix[tong]-prefix[bul2]))
    answer = max(answer,(prefix[tong]-ggul[bul2]-ggul[0]+prefix[tong]-prefix[bul2]))

# case3 통이 중간 어딘가
tong = N-1
for tong in range(1,N-1):
    # print("벌1,벌2,합",prefix[tong]-prefix[0],prefix[-1]-prefix[tong-1]-ggul[-1],(prefix[tong]-prefix[0]+prefix[-1]-prefix[tong-1]-ggul[-1]))
    answer = max(answer,(prefix[tong]-prefix[0]+prefix[-1]-prefix[tong-1]-ggul[-1]))
print(answer)