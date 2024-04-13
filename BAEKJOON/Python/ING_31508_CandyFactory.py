import sys
input = sys.stdin.readline
n,k = map(int, input().split())

# 소팅을 매번 해도 되려나...
# >> 역시 안된다.
# >> 1씩 까보면 알텐데 한방에 min값을 뺀건 최소 사탕 수가 아님 (최대한 모든 사탕을 균일하게 소진해야 정답이 나옴)
# 시간초과를 어떻게 맞출까...


candy = [int(input()) for _ in range(n)]
while len(candy)>=k:
    candy.sort()
    # print(candy)
    candy_min = candy.pop(0)
    if k == 1:
        pass
    else:
        temp = min(candy_min,candy[-k+1]-candy[0]) # 남은 캔디 중 젤 큰놈과 k-1번째 큰놈 비교(min은 pop했으니)
        if temp == 0:
            temp = 1
        for i in range(1,k):
            candy[-i] -= temp
        if candy_min - temp > 0:
            candy.append((candy_min - temp))
    
# print("남은 캔디가 k이하!")
answer = 0
while candy:
    candy.sort()
    # print(candy)
    answer += candy[0]*(k-len(candy))
    candy_min = candy.pop(0)
    for i in range(len(candy)):
        candy[i] -= candy_min
# print(candy)
print(answer)

