def solution(s):
    answer = []
    pre = 0
    post = 0
    temp = 0
    cnt = 0

    while True:
        if s == "1":
            break
        else:
            pre = len(s)
            s = s.replace("0", "")
            post = len(s)
            s = bin(post)
            s = s[2:]
            print(s)
            temp = temp + pre - post
            cnt = cnt + 1
    answer.append(cnt)
    answer.append(temp)
    return answer


# print(solution("110010101001") == [3, 8])
print(solution("01110") == [3, 3])
print(solution("1111111") == [4, 1])
