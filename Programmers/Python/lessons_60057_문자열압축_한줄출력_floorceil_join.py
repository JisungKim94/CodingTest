import math


def solution(s):
    LENGTH = len(s)
    STR, COUNT = 0, 1
    cand = [LENGTH]  # 1~len까지 압축했을때 길이 값

    # LENGTH/2 + 1 보다 더 확인 해 볼 필요는 없으니께
    for size in range(1, math.ceil(LENGTH / 2) + 1):
        compressed = ""
        # string 갯수 단위로 쪼개기 *
        splited = [s[i : i + size] for i in range(0, LENGTH, size)]
        stack = [[splited[0], 1]]
        for unit in splited[1:]:
            if stack[-1][STR] != unit:  # 이전 문자와 다르다면
                stack.append([unit, 1])
            else:  # 이전 문자와 같다면
                stack[-1][COUNT] += 1
        compressed += ("").join(
            [str(cnt) + alphabet if cnt > 1 else alphabet for alphabet, cnt in stack]
        )
        cand.append(len(compressed))
    return min(cand)  # 최솟값 리턴


""" 
한줄 출력
v = list(range(10))

for i in v:
    if i == 10:
        print(i)
    else:
        print("NO")
결과 NO NO NO.... 5 NO NO NO..

print([i if i == 5 else "NO" for i in v])
결과 ['NO', 'NO', 'NO', 'NO', 'NO', 5, 'NO', 'NO', 'NO', 'NO']
"""

print(solution("aabbaccc") == 7)
print(solution("ababcdcdababcdcd") == 9)
print(solution("abcabcdede") == 8)
print(solution("abcabcabcabcdededededede") == 14)
print(solution("xababcdcdababcdcd") == 17)
