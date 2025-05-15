# 걍풀어도 lv1이라 풀리긴 하는데 어렵게 나오면 시간초과 나올수도있어서
# 빠른 풀이가 필요할 수 있음 (예를들면 lessons_12923_숫자블록_약수구하기)
# 빠른풀이 :
# 어떤 수의 약수가 홀수라는 말은 그 수가 다른 수의 제곱수라는걸 의미한다.
# 즉 left이상 right 이하 제곱수들을 찾으면 된다.
# 수열의 합을 이용하면 합도 빠르게 구할 수 있다. https://prgms.tistory.com/57


def numof(num_):
    cnt = 0
    for i in range(1, num_ + 1):
        if (num_ % i) == 0:
            cnt = cnt + 1
    return cnt


def solution(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        if numof(i) % 2 == 0:
            answer = answer + i
        if numof(i) % 2 == 1:
            answer = answer - i
    return answer


print(solution(13, 17) == 43)
print(solution(24, 27) == 52)
