def solve(maxdist):
    l = -(10 ** 9)
    r = 10 ** 9
    for i in range(len(monkeys)):
        for j in range(i + 1, len(monkeys)):
            # dist를 가질 수 있는 ground의 범위를 구하기 위해 필요한 값 
            # 1) 필수로 빠지는 값을 먼저 계산하고~
            groundrange = maxdist - abs(monkeys[i][0] - monkeys[j][0]) - abs(monkeys[i][1] - monkeys[j][1])
            # 2) 주의! 이것만 했는데 벌써 0보다 작으면 이 dist는 불가능 한 값이므로 return false
            if groundrange < 0:
                return 0
            # 3) 필수로 뺄거 빼고 남은걸 2로 나누고 ((y_monkey1 - ground) + (y_monkey2 - ground) 해야하니까 ground는 두 번 쓰인다.)
            groundrange //= 2
            # 4) 위에있는애랑 아래있는애한테 나눈걸 각각 더하고 빼준다. 이게 ground가 위치할 수 있는 range가 된다.
            lower = min(monkeys[i][1], monkeys[j][1]) - groundrange
            upper = max(monkeys[i][1], monkeys[j][1]) + groundrange
            # 5) 이게 구현이 잘 안됐는데 숭이들 조합마다 가지는 lower,upper range가 겹치는 구간이 있는지를 확인하는 과정
            #     [-------]
            #           [-----]
            # [-----]
            # 뭐 위에처럼 ranges가 구성되면 겹치는 구간이 없는거고
            #     [-------]
            #        [-------]
            #    [-----]
            # 이런식으로 구성되면 겹치는 구간이 하나 있다.
            if upper < l or r < lower:
                return 0
            if l <= lower <= r:
                l = lower
            if l <= upper <= r:
                r = upper
    return 1

if __name__ == "__main__":
    n = int(input())
    monkeys = []
    for _ in range(n):
        monkeys.append(list(map(int, input().split())))
    
    # 예상되는 maxdist에 대한 이분탐색
    l = 0
    r = 10 ** 10

    while l <= r:
        maxdist = (l + r) // 2
        if solve(maxdist):
            ans = maxdist
            r = maxdist - 1
        else:
            l = maxdist + 1
    print(ans)
