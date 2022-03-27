import re
from collections import Counter
import math


def clean_text(inputString):
    text_rmv = re.sub(
        "[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`'…》\”\“\’·1234567890]", "", inputString
    )
    return text_rmv


def solution(str1, str2):
    answer = 0
    temp_den = 0
    temp_nom = 0
    ### 정규표현식으로 특수문자 제거
    ### 근데 이 문제에선 이러면 안댐.. 왜냐면 특수문자 있으면 버리는거지 특수문자 제외가 아님
    # str1 = clean_text(str1)
    # str2 = clean_text(str2)
    ### 정규표현식으로 특수문자 제거
    ### 다른 방식으로는 if에 isalpha 사용하는 방법이 있다.
    ### 근데 이 문제에선 이러면 안댐.. 왜냐면 특수문자 있으면 버리는거지 특수문자 제외가 아님

    ### ======================== set을 사용한 집합 사용법 ===============================
    ### ====================== 이 문제에선 set 사용하면 안댐 ============================
    ### ============ 원소의 중복을 허용하는 다중집합에 대해서 확장 했기 때문 ============
    stream_str1 = []
    stream_str2 = []
    for idx, val in enumerate(str1):
        if idx <= len(str1) - 2:
            if str1[idx : idx + 2].isalpha():
                stream_str1.append(str1[idx : idx + 2].lower())
    for idx, val in enumerate(str2):
        if idx <= len(str2) - 2:
            if str2[idx : idx + 2].isalpha():
                stream_str2.append(str2[idx : idx + 2].lower())
    # print(stream_str1)
    # print(stream_str2)
    # stream_str1_set = set(stream_str1)
    # stream_str2_set = set(stream_str2)
    # print((stream_str1_set | stream_str2_set))
    # print((stream_str1_set & stream_str2_set))
    ### ======================== set을 사용한 집합 사용법 ===============================
    ### ====================== 이 문제에선 set 사용하면 안댐 ============================
    ### ============ 원소의 중복을 허용하는 다중집합에 대해서 확장 했기 때문 ============

    ### Counter는 set이 아니지만, or, & 연산 후 len, values 를 사용 해서 합,교집합 구할 수 있다.
    temp_den = Counter(stream_str1) | Counter(stream_str2)
    # print(temp_den.items())
    dem = sum(temp_den.values())
    # print(dem)
    temp_nom = Counter(stream_str1) & Counter(stream_str2)
    # print(temp_nom.items())
    nom = sum(temp_nom.values())
    # print(nom)
    ### Counter는 set이 아니지만, or, & 연산 후 len, values 를 사용 해서 합,교집합 구할 수 있다.

    if dem != 0:
        answer = math.floor(nom / dem * 65536)
    else:
        answer = 65536
    # print(answer)

    return answer


# print(solution("FRANCE", "french") == 16384)
# print(solution("handshake", "shake hands") == 65536)
# print(solution("aa1+aa2", "AAAA12") == 43690)
# print(solution("E=M*C^2", "e=m*c^2") == 65536)
