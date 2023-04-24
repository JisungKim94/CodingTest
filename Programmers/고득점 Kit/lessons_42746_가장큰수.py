def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))


# print(solution([6, 10, 2]))
# print(solution([67, 676, 677]))  # 67767676
# print(solution([3, 30, 34, 5, 9]))  # "9534330"

print(sorted(["55", "333", "99"]))
