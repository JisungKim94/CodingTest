# 이 문제처럼 target == n 으로 주어지는 경우
# 아래와 같이 답을 m이 아닌 l로 사용하면 된다.

def solution(n, times):
    l,r = 1,times[0]*n
    while l<r:
        m = (l+r)//2
        cnt = 0
        for i in times:
            cnt += m//i
        if cnt<n:
            l=m+1
        else:
            r=m

    return l