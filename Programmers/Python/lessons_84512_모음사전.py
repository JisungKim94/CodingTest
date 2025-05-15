def solution(word):
    answer = 0
    vowels = "AEIOU"
    temp = []
    for i in vowels:
        temp.append(i)
        for j in vowels:
            temp.append(i + j)
            for k in vowels:
                temp.append(i + j + k)
                for l in vowels:
                    temp.append(i + j + k + l)
                    for m in vowels:
                        temp.append(i + j + k + l + m)

    answer = temp.index(word) + 1

    return answer


print(solution("A") == 1)
print(solution("AAAAE") == 6)
print(solution("AAAE") == 10)
print(solution("I") == 1563)
print(solution("EIO") == 1189)
