import sys
input = sys.stdin.readline

# attempt 1) 땅은 y방향으로만 움직일 수 있으므로 숭이들의 x좌표는 크게 고려할 필요가 없다. 내가 땅을 움직여도 얘내의 관계를 바꿀순 없으니까
# 모든 숭이들의 y의평균값으로 가는게 젤 좋은 땅인줄 알았는데..
# attempt 2) 예를들어 -1,-3이랑 2,3을 보면 땅을 움직여도 -3~3 사이에서 변하는건 상쇄되면서 둘의 길이에 차이가 없어짐
# 이걸알고 풀면된다. 숭이 좌표가 범위가 크니까 이분탐색으로 접근해야 시간초과 안남
# attempt 3) 근데도 안풀려서 결국 다른사람 풀이를 참고했다. 이분탐색할 오름차순 된 값을 못찾았음
# 일단 프로그래머스 입국심사 문제처럼 답정너 스타일로 이분탐색을 해야한다.
# 이분탐색 진행 과정에서 range로 접근하는 부분이 있는데 이부분 생각을 못했고 구현에도 상당히 애를먹었다.

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
