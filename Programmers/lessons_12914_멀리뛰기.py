def solution(n):
    # 계단 오르는 방식이라고 생각 해 보믄
    stair = [1] + [0] * n
    stair[0], stair[1] = 1, 1
    # n-1 에서 1칸 뛰거나 n-2 에서 2칸 뛰는 것 만이 유일한 n까지 오는 방법
    # 즉 피보나치다.
    # stack으로 풀려고 했더니 시간초과 났음
    for i in range(2, n + 1):
        stair[i] = (stair[i - 1] + stair[i - 2]) % 1234567
    return stair[n]


print(solution(4) == 5)
print(solution(3) == 3)
