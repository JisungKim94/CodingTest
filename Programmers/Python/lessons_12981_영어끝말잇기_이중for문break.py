def solution(n, words):
    answer = []
    pre = words[0][0]
    temp = [[] for _ in range(n)]
    cnt = 0
    iseveryonpass = False
    doublebreakout = False
    for i, v in enumerate(words):
        cnt = cnt % n
        if v[0] == pre[-1]:
            for j in range(n):
                if v in temp[j]:
                    iseveryonpass = False
                    doublebreakout = True
                    break
            temp[cnt].append(v)
            cnt = cnt + 1
            if doublebreakout == True:
                break
            iseveryonpass = True
        else:
            temp[cnt].append(v)
            iseveryonpass = False
            cnt = cnt + 1
            break
        pre = v

    if iseveryonpass == True:
        answer = [0, 0]
    else:
        answer = [cnt, len(temp[cnt - 1])]

    # print(temp)
    # print(answer)
    return answer


# print(
#     solution(
#         3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
#     )
#     == [3, 3]
# )
# print(
#     solution(
#         5,
#         [
#             "hello",
#             "observe",
#             "effect",
#             "take",
#             "either",
#             "recognize",
#             "encourage",
#             "ensure",
#             "establish",
#             "hang",
#             "gather",
#             "refer",
#             "reference",
#             "estimate",
#             "executive",
#         ],
#     )
#     == [0, 0]
# )
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]) == [1, 3])
