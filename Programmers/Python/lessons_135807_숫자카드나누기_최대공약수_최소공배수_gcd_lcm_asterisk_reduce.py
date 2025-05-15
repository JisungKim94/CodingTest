import math
from functools import reduce


def solution(arrayA, arrayB):
    answer = 0
    # 철수가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고 영희가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a
    # 영희가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고, 철수가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a
    # 아래 계산 과정에서 효율적으로 보려면 이래 놔야함
    arrayA = sorted(arrayA, reverse=1)
    arrayB = sorted(arrayB, reverse=1)

    # As of python 3.9 컨테이너 타입의 데이터를 Unpacking 할 때 asterisk(*)를 사용한다.
    # gcd, lcm의 경우 아래와 같이 사용해야만 list 타입을 받을 수 있다.
    # list없이 사용 하려면 math.gcd(1,2,3) list로 사용 하려면 math.gcd(*[1,2,3])
    # 그게 아니라면(python 3.9 이하라면) reduce를 사용해야 한다. https://codechacha.com/ko/python-reduce/
    # "tmp_answer1 = math.gcd(*arrayA)" == "tmp_answer1 = reduce(math.gcd, arrayA)"

    # a = 철수가 가진카드들의 최대공약수
    tmp_answer1 = reduce(math.gcd, arrayA)
    # a = 위에서 구한 값 중 최대값이 영희가 카드로 나눌 수 있는지만 보면 된다. 이때 큰 값 부터 보는게 효율적
    tmp_answer1 = isnotdev(tmp_answer1, arrayB)

    # As of python 3.9 컨테이너 타입의 데이터를 Unpacking 할 때 asterisk(*)를 사용한다.
    # gcd, lcm의 경우 아래와 같이 사용해야만 list 타입을 받을 수 있다.
    # list없이 사용 하려면 math.gcd(1,2,3) list로 사용 하려면 math.gcd(*[1,2,3])
    # 그게 아니라면(python 3.9 이하라면) reduce를 사용해야 한다. https://codechacha.com/ko/python-reduce/
    # "tmp_answer2 = math.gcd(*arrayB)" == "tmp_answer2 = reduce(math.gcd, arrayB)"

    # a = 영희가 가진카드들의 최대공약수
    tmp_answer2 = reduce(math.gcd, arrayB)
    # a = 위에서 구한 값 중 최대값이 철수가 카드로 나눌 수 있는지만 보면 된다. 이때 큰 값 부터 보는게 효율적
    tmp_answer2 = isnotdev(tmp_answer2, arrayA)

    answer = max(tmp_answer1, tmp_answer2)
    # print(answer)
    return answer


# 효율성 때문에 안 쓰는 함수
# 약수 구하는 함수
# 이 방식을 사용하면 tmp_answer1 = reduce(math.gcd, arrayA) 대신 아래와 같은 코드가 필요하고,
# temp1 = devisor(arrayA[-1])
# temp1 = sorted(temp1, reverse=1)
# tmp_answer1 = isdev(temp1, arrayA)
# 이렇게 하면 array의 원소가 100,000,000 일 때 모든 약수를 구하는 과정에서 엄청 큰 계산량이 필요해진다.

# 효율성 때문에 안 쓰는 함수
def devisor(i):
    temp = [i]
    j = 1
    while True:
        if i % j == 0:
            temp.append(j)
        else:
            pass
        if j > i / 2:
            break
        j = j + 1
    return temp


# 효율성 때문에 안 쓰는 함수
def isdev(temp, array):
    res = 1
    cnt = 0
    for i in temp:
        for j in array:
            if j % i == 0:
                res = i
                cnt = cnt + 1
            else:
                res = 1
                cnt = 0
                break
        if cnt == len(array):
            break
    return res


def isnotdev(temp, array):
    res = 0
    for j in array:
        if j % temp == 0:
            res = 0
            break
        else:
            res = temp
    return res


print(solution([10, 17], [5, 20]) == 0)
print(solution([10, 20], [5, 17]) == 10)
print(solution([14, 35, 119], [18, 30, 102]) == 7)
