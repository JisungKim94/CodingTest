def solution(s):
    answer = s

    numb_ = [
        ["zero", "0"],
        ["one", "1"],
        ["two", "2"],
        ["three", "3"],
        ["four", "4"],
        ["five", "5"],
        ["six", "6"],
        ["seven", "7"],
        ["eight", "8"],
        ["nine", "9"],
    ]

    for i, j in numb_:
        s = s.replace(i, j)

    answer = int(s)

    return answer


print(solution("one4seveneighteight") == 14788)
# print(solution("23four5six7")==234567)
# print(solution("2three45sixseven")==234567)
# print(solution("123")==123)
