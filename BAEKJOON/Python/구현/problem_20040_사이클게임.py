# 그냥 그래프 문제인듯..
# 근데 못풀겠다. 자료구조에 확실히 약하다.. union find나 disjoint set 문제라고 함 cylce 판단하기
# https://ip99202.github.io/posts/유니온-파인드(Union-Find)/
# 아래가 가장가장 기본꼴 이므로 이걸 잘 공부 해 봅시다잉


import sys

def find_parent(x):
    while x != parent[x]:
        x = parent[x]
    return x
# 작성

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
# 작성

input = sys.stdin.readline
n, m = map(int, input().split())
parent = list(range(n))

for i in range(m):
    x, y = map(int, input().split())
    if find_parent(x) == find_parent(y):  # 사이클 발생시
        print(i + 1)
        break
    union(x, y)  # 점 잇기
    # print(parent)
else:  # m번의 차례를 모두 처리한 이후에도 종료되지 않았다면
    print(0)

