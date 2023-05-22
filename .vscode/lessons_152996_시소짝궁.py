def solution(weights):
    answer = 0
    temp = [0] * 1001
    for i, weight in enumerate(weights):
        temp[weight] = temp[weight] + 1

    for i, v in enumerate(temp):
        if temp[i] > 0:
            answer = answer + (temp[i] * (temp[i] - 1)) // 2
        if i * 2 / 3 == i * 2 // 3:
            answer = answer + v * temp[i * 2 // 3]
        if i * 3 / 4 == i * 3 // 4:
            answer = answer + v * temp[i * 3 // 4]
        if i / 2 == i // 2:
            answer = answer + v * temp[i // 2]

    return answer
