def solution(msg):
    answer = []
    dic = {}

    # AtoZ dic
    for i in range(26):
        dic[chr(65 + i)] = i + 1

    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w : c + 1] not in dic:
            dic[msg[w : c + 1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer


print(solution("KAKAO") == [11, 1, 27, 15])
print(
    solution("TOBEORNOTTOBEORTOBEORNOT")
    == [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
)
print(solution("ABABABABABABABAB") == [1, 2, 27, 29, 28, 31, 30])
