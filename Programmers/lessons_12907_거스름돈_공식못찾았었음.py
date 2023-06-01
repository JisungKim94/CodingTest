def solution(n, money):
    temp = [0] * (n + 1)
    temp[0] = 1

    for i in money:
        for j in range(i, n + 1):
            if j >= i:
                temp[j] = temp[j] + temp[j - i]

    return temp[-1] % 1000000007
