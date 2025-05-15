import sys
input = sys.stdin.readline
N,HP = map(int,input().split())
skills = [list(map(int,input().split())) for _ in range(N)]
answer = 100001
cnt = [0]*len(skills)
def dfs(HP,cnt,time):
    global answer
    # print(HP,cnt,time)
    if HP<=0 or time>answer:
        answer = min(answer,time)
        # print(HP,time)
        return
    for i in range(len(cnt)):
        if cnt[i]>0:
            cnt[i]-=1
    flag = 1
    for i in range(len(skills)):
        if cnt[i]==0:
            cnt[i]=skills[i][0]
            dfs(HP-skills[i][1],cnt[::],time+1)
            cnt[i]=0
            flag = 0
    if flag:
        dfs(HP,cnt[::],time+1)

dfs(HP,cnt,0)
print(answer)