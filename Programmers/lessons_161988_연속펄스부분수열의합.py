# 하루정도 품..
# 핵심은 어차피 펄스 처리를 해 줘도 총 합은 음, 양의 차이만 생긴다.
# 누적합을 펄스 규칙 중 하나에 따라서 구해주고 가장 큰 구간을 뽑을 수 있게 하면 된다.


def solution(sequence):
    answer = sequence[0]
    l = 0
    r = 0
    temp = 0
    prefix_sequence = [0]
    for i, v in enumerate(sequence):
        if i % 2 == 0:
            temp = temp + v
        else:
            temp = temp - v
        prefix_sequence.append(temp)
    # print(prefix_sequence)
    # print(prefix_sequence[r+1]-prefix_sequence[l])

    answer = abs(min(prefix_sequence) - max(prefix_sequence))

    return answer


print(solution([2, 3, -6, 1, 3, -1, 2, 4]) == 10)
