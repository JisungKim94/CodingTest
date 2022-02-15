import math


def check_cutable(s):
    start_ = 0
    end_ = 0
    compressed_num_ = []
    for i in range(1, int(math.floor(len(s) / 2)) + 1, 1):
        # print(i)
        # print(s[0:i])
        # print(s[i : i + i])
        for j in range(0, len(s), i):
            end_ = end_ + i
            if (s[start_:end_]) == (s[start_ + i : end_ + i]) and (
                i not in compressed_num_
            ):
                compressed_num_.append(i)
            start_ = start_ + i
        start_ = 0
        end_ = 0
    return compressed_num_


def solution(s):
    start = 0
    end = 0
    cur = ""
    pre = ""
    cnt_1 = 0
    cnt_2 = 0
    temp_answer_1 = 0
    temp_answer_2 = 0
    answer_list = []
    checker = False

    compressed_num = check_cutable(s)
    print(compressed_num)

    if compressed_num:
        for i in compressed_num:
            for _ in range(0, len(s), i):
                end = end + i
                if end <= len(s):
                    cur = s[start:end]
                    start = start + i

                    if cur == pre:
                        cnt_1 = cnt_1 + 1
                        checker = True

                    if checker == True:
                        if cur != pre:
                            cnt_2 = cnt_2 + 1
                            checker = False
                    pre = cur
                    if checker == True and start == len(s):
                        cnt_2 = cnt_2 + 1

            # print(cnt_1)
            temp_answer_1 = cnt_1 * i  # 숫자로 압축 하면서 줄어든 문자열 개수
            print(cnt_1)

            temp_answer_2 = cnt_2  # 압축했을 때 숫자 종류 수
            print(temp_answer_2)
            print("==========")
            answer_list.append(len(s) - temp_answer_1 + temp_answer_2)
            start = 0
            end = 0
            cnt_1 = 0
            cnt_2 = 0
            cur = ""
            pre = ""
            checker = False
            temp_answer_1 = 0
            temp_answer_2 = 0
        print(answer_list)
        answer = min(answer_list)
    else:
        answer = len(s)
    return answer


"""
2a2ba3c
7

2ab2cd2ab2cd
12
2ababcdcd
9

abcabc2de
9

abcabc2de
9
2abcdede
8
"""


# print(solution("aabbaccc") == 7)
# print(solution("ababcdcdababcdcd") == 9)
# print(solution("abcabcdede") == 8)
# print(solution("abcabcabcabcdededededede") == 14)
# print(solution("xababcdcdababcdcd") == 17)
