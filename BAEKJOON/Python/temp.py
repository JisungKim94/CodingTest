# 그냥 그래프 문제인듯..
# 근데 못풀겠다. 자료구조에 확실히 약하다.. union find나 disjoint set 문제라고 함 cylce 판단하기
# https://ip99202.github.io/posts/유니온-파인드(Union-Find)/
# 아래가 가장가장 기본꼴 이므로 이걸 잘 공부 해 봅시다잉


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = list(range(n))
