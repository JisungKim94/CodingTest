# 다시..
# 걍 쉽게 생각하면 시간초과 남
# 일단 newroads를 0으로 초기화 하면 size가 커져서 시간초과나고
# set을 쓰면 좀 낫긴 한데 같은 O(1) 이래도 배열이 경험적으로 더 빠르다고 함
# djikstra 할 때 뭔가 좀 다름...
# 시작에 초점을 맞추면 각각 돌려야대서 시간초과나고 destination에서 올라오는 방식으로 한 번에
# 찾나..? 이게 cost가 1로 동일해서 글너거 같기도 하고..
# 글고 deque 가 heapq보다 빠름 어차피 cost1이니까 popleft, append 사용하면 더 빠르다고 함 ㅁㄴㄷㅇㄹ;
from collections import deque


def solution(n, roads, sources, destination):
    newroads = [[] for _ in range(n + 1)]
    for x, y in roads:
        newroads[x].append(y)
        newroads[y].append(x)

    dist = [-1] * (n + 1)
    dist[destination] = 0
    que = deque([destination])
    while que:
        node = que.popleft()
        next_node_d = dist[node] + 1
        for y in newroads[node]:
            if dist[y] == -1:
                dist[y] = next_node_d
                que.append(y)

    return [dist[i] for i in sources]
