def solution(brown, yellow):
    answer = []
    width = 0
    height = 0
    num_brown = 0
    for i in range(yellow):
        height = i + 1
        width = int(yellow / height)
        num_brown = (width + height) * 2 + 4
        if (num_brown == brown) & (width * height == yellow):
            answer = [width + 2, height + 2]
            break

    print(answer)
    return answer


print(solution(10, 2) == [4, 3])
print(solution(8, 1) == [3, 3])
print(solution(24, 24) == [8, 6])
print(solution(28, 36) == [8, 8])
