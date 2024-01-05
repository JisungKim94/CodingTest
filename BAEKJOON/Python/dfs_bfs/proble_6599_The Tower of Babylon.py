# 쉬운 위상정렬 문제 풀어보려고 건드렸는데 뭔..
# 개어려운 dp였네 아닌가;;...


def isStackable(lowerstone, lowerwlh, upperstone, upperwlh, stones):
    # wlh는 width, length, height 중 높이로 사용할 인자 선택용
    lower,upper = [],[]
    for m in range(3):
        if m != lowerwlh:
            lower.append(stones[lowerstone][m])
    for m in range(3):
        if m != upperwlh:
            upper.append(stones[upperstone][m])
            
    if max(lower) > max(upper) and min(lower) > min(upper):
        return True
    return False

def dyprog(lowerstone, lowerwlh, stones, dp):
    # wlh는 width, length, height 중 높이로 사용할 인자 선택용
    if dp[lowerstone][lowerwlh] != 0:
        return dp[lowerstone][lowerwlh]
    
    ans = stones[lowerstone][lowerwlh]
    for upperstone in range(N):
        for upperwlh in range(3):
            if isStackable(lowerstone, lowerwlh, upperstone, upperwlh, stones):
                ans = max(ans, dyprog(upperstone, upperwlh, stones, dp) + stones[lowerstone][lowerwlh])
    
    # 더이상 쌓을거 없으면 걔부터 높이 측정
    dp[lowerstone][lowerwlh] = ans
    # print(dp)
    return ans

if __name__ == "__main__":
    case = 0
    while True:
        N = int(input())
        if N == 0:
            break
        
        maxh = 0
        stones = [[0] * 3 for _ in range(N)]
        dp = [[0] * 3 for _ in range(N)]
        
        for i in range(N):
            stones[i] = list(map(int, input().split()))
        
        # print(stones)
        for i in range(N):
            for j in range(3):
                maxh = max(maxh, dyprog(i, j, stones, dp))
                
        
        case += 1
        print(f"Case {case}: maximum height = {maxh}")
