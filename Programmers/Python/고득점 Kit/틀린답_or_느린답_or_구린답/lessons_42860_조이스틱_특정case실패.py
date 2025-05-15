alpabet = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 12,
    "P": 11,
    "Q": 10,
    "R": 9,
    "S": 8,
    "T": 7,
    "U": 6,
    "V": 5,
    "W": 4,
    "X": 3,
    "Y": 2,
    "Z": 1,
}


def solution(name):
    answer = 0
    cnt_right = 0
    cnt_left = 0
    is_find_right = False
    is_find_left = False

    for idx, name_ in enumerate(name):
        answer = answer + alpabet[name_]
        if idx == 0:
            pass
        else:
            if name[idx] != "A" and is_find_right == False:
                cnt_right = idx
                is_find_right = True
            if name[-idx] != "A" and is_find_left == False:
                cnt_left = -idx
                is_find_left = True

    if cnt_right > cnt_left and (cnt_right != 0 and cnt_left != 0):
        answer = answer + len(name) - cnt_right
    elif cnt_right < cnt_left and (cnt_right != 0 and cnt_left != 0):
        answer = answer + len(name) - (-cnt_left)

    # print(answer, cnt_right, cnt_left)
    return answer


# solution("JAN")
# solution("JEROEN")
# solution("JAAXAAANA")
print(solution("ZZAAAZZ"))  # 답은 8 이미 지나간 곳을 다시 지나가는게 더 빠른 경우
