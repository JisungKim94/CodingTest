def solution(sticker):
    answer = 0
    if len(sticker) <= 3:
        return max(sticker)
    if (sticker[0] + sticker[2] + sticker[-2]) > (
        sticker[1] + sticker[3] + sticker[-1]
    ):
        temp = 0
        indexing = range(1, len(sticker) - 1)
    else:
        temp = 1
        indexing = range(2, len(sticker))

    dp = [0] * len(sticker)
    if temp == 0:
        dp[0] = sticker[0]
    else:
        dp[1] = sticker[1]

    for i in indexing:
        dp[i] = max(sticker[i] + dp[i - 2], dp[i - 1])

    print(dp)
    return max(dp[-2], dp[-1])
