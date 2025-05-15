def solution(n):
    ans = []
    i = n
    cnt = 0
    if n == 1:
        ans = 1
    else:
        while i >= 3:
            if i % 2 == 0:
                i = i // 2
                # print(i, cnt)
            else:
                i = i - 1
                cnt = cnt + 1
                # print(i, cnt)
            if i == 3:
                ans = 2 + cnt
            if i == 2:
                ans = 1 + cnt
    # print(ans)
    return ans


def solution2(n):
    return bin(n).count("1")


print(solution(5) == 2)
print(solution(6) == 2)
print(solution(7) == 3)
print(solution(8) == 1)
print(solution(9) == 2)
print(solution(5000) == 5)
