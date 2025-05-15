def solution(numbers):
    answer = []

    for number in numbers:
        # 짝수일 경우 마지막에 1 추가
        # list(bin(number)[2:]) << 개꿀이네 이거
        if number % 2 == 0:
            binary_num = list(bin(number)[2:])
            binary_num[-1] = "1"
        # 홀수일 경우 오른쪽부터 찾아야 대는데 이걸 몰랐음
        # rfind 를 이용하면 된다.
        else:
            binary_num = bin(number)[2:]
            binary_num = "0" + binary_num
            one_idx = binary_num.rfind("0")
            binary_num = list(binary_num)
            binary_num[one_idx] = "1"
            binary_num[one_idx + 1] = "0"

        ans_num = int("".join(binary_num), 2)
        answer.append(ans_num)

    return answer


print(solution([2, 7]) == [3, 11])
# print(solution([0, 1, 3, 4, 5, 6]) == [1, 2, 4, 5, 6, 7])
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [3, 11])
print(
    solution(
        [
            1001,
            337,
            0,
            1,
            333,
            673,
            343,
            221,
            898,
            997,
            121,
            1015,
            665,
            779,
            891,
            421,
            222,
            256,
            512,
            128,
            100,
        ]
    )
    == [
        1002,
        338,
        1,
        2,
        334,
        674,
        347,
        222,
        899,
        998,
        122,
        1019,
        666,
        781,
        893,
        422,
        223,
        257,
        513,
        129,
        101,
    ]
)
