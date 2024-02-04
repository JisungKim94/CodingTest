import sys
sys.setrecursionlimit(10 ** 8)
N = int(input())
jobs = list(map(int, input().split()))
# print(jobs)

# 금요일에 일이 끝나면 헬스장 -> 적절히 순서를 바꿀수 있음 -> 합의 mod가 ~면 금요일 음... 모든 케이스를 해야할듯(브루트포스+백트래킹)?
# 시간초과가 나니까 bfs로 탐색?
# 걍 탐색 자체가 아니고 다른 방식으로 접근?
# 어캐 걍 비벼서 풀었는데 다른풀이를 보니 왜 빨리 생각이 안났을까 싶네.. ㅠㅠ

for i in range(len(jobs)):
    jobs[i]%=7
    
dic = {}
for job in jobs:
    dic[job] = dic.get(job,0) + 1

week = [0]*7
for v1 in dic:
    indice = [0]
    for i,v in enumerate(week):
        if v == 1:
            indice.append(i)
    # print(indice)
    for idx in indice:
        temp = dic[v1]
        while temp > 0:
            idx = (idx+v1)%7
            week[idx] = 1
            if week[4]==1:
                break
            temp-=1
    if week[4]==1:
        break
# print(week)
    
    
if week[4]==1:
    print("YES")
else:
    print("NO")