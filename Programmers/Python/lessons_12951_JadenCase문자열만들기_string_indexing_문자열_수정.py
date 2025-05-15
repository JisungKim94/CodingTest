def solution(s):
    answer = ""
    temp = []

    s = s.split(" ")
    for i in s:
        i = i.lower()
        tmp = list(i)
        if tmp:
            tmp[0] = tmp[0].upper()
            i = "".join(tmp)
        else:
            pass
        temp.append(i)

    answer = " ".join(temp)

    return answer


# print(solution("3people unFollowed me") == "3people Unfollowed Me")
print(solution("3people  unFollowed me") == "3people  Unfollowed Me")
# print(solution("for the last week") == "For The Last Week")
