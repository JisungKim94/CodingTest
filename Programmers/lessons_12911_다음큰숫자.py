def solution(n):
    answer = 0
    n = list(bin(n))[2:]
    # print(n)
    n.reverse()
    # print(n)
    cnt = 0
    check = False
    for i, v in enumerate(n):
        if n[i] == "1":
            check = True
        elif n[i] == "0":
            if check == True:
                n[i] = "1"
                n[i - 1] = "0"
                cnt = i
                break
    if cnt == 0:
        n.append("1")
        n[-2] = "0"
        cnt = len(n)
    # print(n, cnt)
    cnt2 = 0
    for i in range(cnt - 1):
        if n[i] == "1":
            n[i] = "0"
            cnt2 = cnt2 + 1

    for i in range(cnt - 1):
        if n[i] == "0" and cnt2 > 0:
            n[i] = "1"
            cnt2 = cnt2 - 1

    # print(n)
    n.reverse()
    # print(n)
    # print(int("0b" + "".join(n), base=0))
    answer = int("0b" + "".join(n), base=0)
    return answer


# print(solution(78) == 83)
# print(solution(15) == 23)
# print(solution(76) == 81)
print(solution(6) == 9)

# print(int("0b110", base=0))
# print(int("0b1001", base=0))
