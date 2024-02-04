import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 위상정렬 문제이지 않을까? 음 누가 누굴 이겼다는 정보가 없어서 그래프를 못그려서 힘들거같다.
# 완전탐색으로 백트래킹 하면서 풀면 될거같은데... 구현을 못했다 gg!!!


# 알고리즘만 보고 구현 해 보기
# a,b가 싸웠을 때 결과는 a승b패, a무b무, a패b승 총 3가지이고 총 경기 수는 5+4+3+2+1 = 15경기 즉 3^15짜리 탐색이다.
# AB, AC, AD, AE, AF, BC, BD ... 순서대로 3개씩 확인 하고 그때마다 results에 승,무,패쪽을 알맞게 빼준다.
# 만약 results의 elments중 -1이 나오거나 끝났는데 남아있는게 있다면 불가능한 케이스
answer = [0,0,0,0]
def dfs(home,away):
    if away>5:
        home+=1
        away=home+1
    if home==5:
        temp = 0
        for result in results:
            temp+=sum(result)
        if temp == 0:
            answer[idx]=1
        return
    # win
    if results[home][0]>0 and results[away][2]>0:
        results[home][0]-=1
        results[away][2]-=1
        dfs(home,away+1)
        results[home][0]+=1
        results[away][2]+=1
    # draw
    if results[home][1]>0 and results[away][1]>0:
        results[home][1]-=1
        results[away][1]-=1
        dfs(home,away+1)
        results[home][1]+=1
        results[away][1]+=1
    # losd
    if results[home][2]>0 and results[away][0]>0:
        results[home][2]-=1
        results[away][0]-=1
        dfs(home,away+1)
        results[home][2]+=1
        results[away][0]+=1
for idx in range(4):
    info = map(int, input().split())
    results = [[0]*3 for _ in range(6)]
    row,col = -1,-1
    for i,v in enumerate(info):
        if i%3 == 0:
            row+=1
            col=0
        results[row][col] = v
        col+=1
    dfs(0,1)
print(*answer)