from itertools import combinations


def is_prime(input_):
    answer = True
    if input_ == 1 or input_ == 0:
        answer = False
    else:
        for j in range(2, input_):
            temp = input_ % j
            if temp == 0:
                answer = False
                break
    return answer


def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3))
    for i in comb:
        if is_prime(sum(i)) == True:
            answer = answer + 1
    return answer


print(solution([1, 2, 3, 4]) == 1)
print(solution([1, 2, 7, 6, 4]) == 4)
