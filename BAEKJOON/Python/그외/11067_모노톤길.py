import sys

input = sys.stdin.readline

# x,y가 10만이고 곱하면 엄청 크니까 board만들어서 dfs할 생각을 안 했어야 함
# sorting을 잘 해보자
T = int(input())

for i in range(T):   
    N = int(input())    
    dic = {}
    X = 0
    for j in range(N):
        x, y = map(int, input().split())
        X = max(x,X)
        if x not in dic:
            dic[x] = list()
        dic[x].append(y)
    
    answer = []
    sorteddic = sorted(dic.items())
    # print(sorteddic)
    for idx,item in enumerate(sorteddic):
        if len(item[1])==1:
            answer.append((item[0],item[1][0]))
        else:
            if answer:
                prey = answer[-1][1]
            else:
                prey = 0
                
            if prey<=item[1][0] and prey<=item[1][1]:
                item[1].sort(reverse=1)
                while item[1]:
                    answer.append((item[0],item[1].pop()))
            else:
                item[1].sort(reverse=0)
                while item[1]:
                    answer.append((item[0],item[1].pop()))
    # print(answer)
    
    
    m = list(map(int, input().split()))
    # print(m)
    for i in range(1,len(m)):
        print(answer[m[i]-1][0],answer[m[i]-1][1])