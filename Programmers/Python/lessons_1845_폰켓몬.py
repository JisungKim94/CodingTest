def solution(nums):
    answer = 0

    answer = len(nums) / 2

    nums = set(nums)
    if len(nums) < answer:
        answer = len(nums)

    return answer


print(solution([3, 1, 2, 3]) == 2)
print(solution([3, 3, 3, 2, 2, 4]) == 3)
print(solution([3, 3, 3, 2, 2, 2]) == 2)
