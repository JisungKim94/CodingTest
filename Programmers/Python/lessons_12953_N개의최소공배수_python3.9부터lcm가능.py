import math


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def solution(arr):
    answer = 0
    stack = []

    for i in arr:
        if not stack:
            stack.append(i)
        else:
            stack.append(lcm(stack.pop(), i))
        print(stack)

    return stack[-1]


print(solution([2, 6, 8, 14]) == 168)
print(solution([1, 2, 3]) == 6)
