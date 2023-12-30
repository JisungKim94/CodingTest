import sys
input = sys.stdin.readline

# 1) hashtable 로 시도
# 2) 원래는 입차,출차 순서로 풀어보려다가 실패(시간낭비)
# 3) 데이터고 시간이고 모르겠고 내 앞에 있던차였는지 전부확인
# 4) 1000 개짜리니까 애초에 개무시하고 풀었어야 하는듯..

# 5) 사실 이렇게 할 필요가 없고..
# 아래와 같은 구조처럼 이중 for문에 두번째 for문 시작조건만 고쳐줬으면 됐었음...
# cnt = 0
# innumbers = {} (O(1) 하려고 dict로 구성해주고)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if innumbers[outnumbers[i]] > innumbers[outnumbers[j]]:
#             cnt += 1
#             break

N = int(input())
answer = 0
numbers = [input().strip() for _ in range(2*N)]
innumbers = numbers[:N]
outnumbers = numbers[N:]
# print(innumbers)
# print(outnumbers)
dic = {}
frontcar = []
checked = {}
for v in innumbers:
    dic[v] = []
    checked[v]=0
    for i in frontcar:
        dic[v] += [i]
    frontcar.append(v)
# print(dic)
frontcar = []
for v in outnumbers:
    for i in frontcar:
        if i in dic[v]:
            pass
        else:
            checked[i]=1
    frontcar.append(v)

# print(checked)
for i in checked:
    if checked[i]==1:
        answer+=1
print(answer)