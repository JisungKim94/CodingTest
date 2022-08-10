# # 10진수 -> 2~16진수까지 변환
# 코테 보는 애들은 걍 외워서 쓰는듯
# def convert(num, base):
#     tmp = '0123456789ABCDEF'
#     q, r = divmod(num, base)
#     if q == 0:
#         return tmp[r]
#     else:
#         return convert(q) + tmp[r]
# 뒤집기 : arr[::-1]
# n진법 -> 10진법 : int(num, n)


def solution(n):
    answer = []

    while n > 0:
        n, re = divmod(n, 3)  # n을 3으로 나눈 몫과 나머지
        answer.append(str(re))

    # 뒤집는 방법
    # 1. arr[::-1] : 뒤집힌 answer, 사용 하려면 이 값을 써야함
    # 2. answer.reverse() : 반환 없음 answer 값은 뒤집힘
    # 3. reversed(answer) : 뒤집힌 answer를 반환
    # 근데 알고보니 이 문제에선 append라서 뒤집을 필요 없었음

    answer = "".join(answer)
    # print(answer)
    return int(answer, 3)


print(solution(45) == 7)
print(solution(125) == 229)
