import sys
input = sys.stdin.readline
N, M = map(int, sys.stdin.readline().rstrip().split())
relationships = [list(map(int, input().split())) for _ in range(M)]

# K각 관계를 이루지 않게 = cycle 형성을 막아라..
# 최소신장트리 (MST) 크루스칼

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



relationships.sort(reverse=1,key= lambda x: x[2])
# print(relationships)
parent = list(range(N+1))
answer = 0
for a,b,c,d in relationships:
    if d == 1:
        union(parent, a, b)  # 점 잇기
for a,b,c,d in relationships:
    # print(a,b,c,d,find_parent(parent, a) == find_parent(parent, b))
    if d==1:
        continue
    if find_parent(parent, a) == find_parent(parent, b):  # 사이클 발생시
        answer+=c
        continue
    union(parent, a, b)  # 점 잇기
# print(parent)
print(answer)