from itertools import permutations


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


def solution(numbers):
    temp_0 = ""
    temp_1 = []
    cnt = 0
    for i in range(1, len(numbers) + 1):
        temp = list(permutations(numbers, i))
        for j in temp:
            for k in j:
                temp_0 += k
            temp_1.append(int(temp_0))
            temp_0 = ""
    temp_1 = list(set(temp_1))
    # print(temp_1)
    for i in temp_1:
        if is_prime(i) == True:
            cnt = cnt + 1

    return cnt


# print(is_prime(1))
print(solution("17"))
# print(solution("011"))
