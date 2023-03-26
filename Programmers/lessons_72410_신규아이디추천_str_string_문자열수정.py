""" 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
특수문자 : -_.~!@#$%^&*()=+[{]}:?,<>/ """


# 문자열 치환 하려면 for문으로 하나 씩 빼서 list에 한개씩 넣는 과정에서
# 수정된 애를 사용하는 느낌


def solution(old_id):
    answer = ""
    new_id = ""
    pre_val = ""
    symbols = '~!@#$%^&*()=+[{]}:?,<>/ """'

    # seq 1
    old_id = old_id.lower()  # 소문자로 바꾸기

    # seq 2, 3
    for idx, val in enumerate(old_id):
        if symbols.find(val) == -1:  # 특수문자 제거
            if (pre_val == ".") & (val == "."):  # . 2개 하나로 치환
                pass
            else:
                new_id = new_id + val
                pre_val = val

    print(new_id)
    # seq 4
    new_id = list(new_id)
    while len(new_id) != 0 and (new_id[0] == "."):
        new_id.pop(0)
    while len(new_id) != 0 and (new_id[-1] == "."):
        new_id.pop()
    # seq 5
    if not new_id:
        new_id = ["a"]

    # seq 6
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == ".":
            new_id.pop()

    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id.append(new_id[-1])

    # seq 7
    for i in new_id:
        answer = answer + i
    # 으이구 등쉰아.. join 쓰면 대자나
    # answer = "".join(new_id)

    print(old_id)
    print(new_id)
    print(answer)

    return answer


# print(solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi")
# print(solution("z-+.^.") == "z--")
# print(solution("=.=") == "aaa")
# print(solution("123_.def") == "123_.def")
# print(solution("abcdefghijklmn.p") == "abcdefghijklmn")
print(solution("-.~/.-") == "-.-")
