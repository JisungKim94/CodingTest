import math


def convert(num, base):
    tmp = "0123456789ABCDEF"
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


# https://geekflare.com/prime-number-in-python/ (5 제곱근을 이용한 소수판별)
def isprime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False
    return num > 1


def solution(n, k):
    answer = 0

    temp = convert(n, k)
    # print(temp)
    temp = temp.split("0")
    # print(temp)
    for i in temp:
        if i == "":
            pass
        else:
            if isprime(int(i)) == True:
                answer = answer + 1
    print(answer)
    return answer


print(solution(437674, 3) == 3)
print(solution(110011, 10) == 2)
