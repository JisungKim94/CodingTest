def solution(n, stations, w):
    answer = 0
    received = 0
    answer = 0
    for i in stations:
        while received < i - w - 1:
            received = received + (2 * w + 1)
            answer = answer + 1
            # print(received, answer)
        received = i + w
    if received < n:
        while received < n:
            received = received + (2 * w + 1)
            answer = answer + 1

    return answer


print(solution(11, [4, 11], 1) == 3)
print(solution(10, [7, 9], 1) == 2)
print(solution(16, [9], 2) == 3)
print(solution(16, [1], 1) == 5)
print(solution(13, [3, 7, 11], 1) == 4)
print(solution(16, [1, 16], 2) == 2)
