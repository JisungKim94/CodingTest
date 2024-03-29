""" 양과 늑대는 서로 천적인가 봅니다.
레이튼교수 시리즈에도 양과 늑대를 가지고 강을 건너는
이 문제와 상당히 유사했던 문제가 있었습니다.

이 문제의 시작은 0번 정점은 항상 양으로 시작합니다.
당연히 늑대로 1빠따로 시작하면 양을 한 마리도 못 모으기 때문이죠.
그럼 우리는 답을 전부 0으로 제출하면 되니까 개꿀이기는 하지만, 카카오로 상대로는 어림도 없습니다.
아쉽게도 양이 항상 0번 노드를 차지해서 양을 모으는 경우의 수가 생기겠군요 ㅠㅠ

단순히 생각해봐도, 완전탐색에 해당되는 문제입니다.
그것도 모든 경우의 수를 탐색하는 문제가 됩니다.
따라서 BFS나 DFS나 어떤 걸 사용하셔도 무방하지만,
사실 BFS를 사용하려면 큐도 소환해야하고, 데이터 푸쉬하고, 팝하고 어지간히 귀찮습니다.
그냥 간단하게 DFS를 사용하여 구현하는 것이 편할겁니다.

그럼 우리는 이제 DFS를 어떤식으로 돌리면 좋을까? 라는 생각을 먼저 하게 됩니다.
이 문제를 보자면, 이미 지났던 정점들을 다시 한 번 지나가서 반대편으로 넘어가서 양을 데려오기도 하고,
아무튼, 역류해서 다시 다른 쪽으로 지나가는 상황이 연출되는 것을 쉽게 알 수 있습니다.
그래서 대부분, 양방향 그래프를 사용해야겠군, 이라고 생각하여, 코딩을 하다가, 재귀호출스택을 초과하거나,
실행시간 10초를 넘겨 프로그래머스 채점 시스템한테 엄청난 싸다구를 맞게 됩니다.

근데 단순히 생각해보자면, 이미 지나갔던 정점은 생각해봤을 때, 다시 방문하더라도,
아무런 변화가 없습니다. 왜냐하면 최초방문시에 해다 정점에 서식했던 동물이 따라오게 때문이고,
그게 게임이 끝날 때 까지 계속 따라 다니기 때문입니다. 같은 정점을 다시 방문해도 결국에는, 아무런 의미가 없습니다.
그럼 우리는 굳이 양방향 그래프를 써가면서, 무한적인 재귀호출을 만들 필요는 없습니다.
그러면, 단방향 그래프를 통하여, 재귀호출을 구현할 수 있는 방법을 찾을 필요가 존재합니다.
바로 그 답은, 다음 차례에 이동 가능한 정점을 따로 담아서 재귀호출을 하는 것입니다.

자, 첫번째 테스트 케이스를 예시로 들어보도록 하겠습니다.
0번 정점은 1번과 8번 정점을 자식으로 두고 있습니다. 즉, 쉽게 말하면, 0번 정점을 한 번 들렸다는 의미는,
1번과 8번 정점을 다시 언제든지 방문할 수 있게 됩니다. 부모 정점을 방문하여 이미 길이 만들어졌으면,
그 부모 정점의 하나 바로 밑에 존재하는 자식 정점들은 언제든지 입장이 가능하게 됩니다.
그럼 만약에 1번과 8번 정점을 갈 수 있다고 하면 나는 지금 당장 8번 정점으로 이동한다고 가정하여 봅시다.
다음에 갈 수 있는 정점은 [1, 8] 에서 [1, 7, 9] 정점이 됩니다. 0번 정점을 최초로 방문한 후에
다음에 갈 수 있는 정점을 계산하면, [1, 8]번 정점을 방문할 수 있게 됩니다. 또한 8번 정점을 방문하게 되면,
8번 정점을 리스트에서 제하고(방문했으므로) 8번 정점의 자식들인 7번과 9번 정점이 추가 되어서,
최종적으로 [1, 7, 9]번 정점들을 방문할 수 있게 됩니다. 이런 방법이면, 굳이 그래프가 역류하는 경우를 계산 할 필요가
없게 됩니다. 또한 모든 그래프를 전부 방문하게 되면 자연스럽게 다음에 방문할 수 있는 그래프가 존재하지 않게 되므로,
재귀호출이 일어나지 않습니다.

수행 1.

graph의 기초 틀을 만든다. 인접리스트 방식을 추천한다. graph[부모정점] 와 같이 접근하면 자식 값들을 반환하는 형태로 제작된다. info의 길이가 5인 경우 초기값 = [[], [], [], [], []] 와 같이 된다.
수행 2.

edge배열을 가지고, 그래프에 각각 데이터를 입력한다. edge첫번째 요소는, 부모정점, 두번째 요소는 자식정점이다. graph[부모정점].add(자식정점)과 같이 부모정점위치에 자식정점의 요소를 추가해준다.
수행 3.

결과를 저장할 변수를 선언한다. 초기값은 0아니면 1(마음대로 해라.. 2이상은 안된다.)
수행 4.

dfs함수를 만든다. 함수의 인수들을 정한다. (현재 정점, 양의 수, 늑대의 수, 이동가능한 정점들) 대충 이와 같은 인수를 갖게된다. 먼저 현재 정점을 가지고, info에 정점값을 인덱스로 집어넣어 늑대인지 양인지 판단하고, 양 또는 늑대의 카운트를 하나 올린다. 그 다음에는, 결과를 저장하는 변수보다 양의 수가 더 많으면 결과변수를 현재 양의 수로 값을 업데이트한다. 만약 늑대의 수가 양의 수보다 같거나, 크면, 함수를 리턴 한다. 더 이상 수행하면 답을 구할 수 없기 때문이다. 그 다음에는 현재 이동가능한 정점들에서 현재 정점의 자식 정점들을 추가한다. 왜냐하면 현재 정점을 방문했기 때문에, 현재 정점의 자식 정점들을 탐색할 수 있는 권한이 주어졌기 때문이다. 길이 뚫린 것이다. 하하 for문으로 이동가능한 정점들을 탐색하면서, 하나씩 해당 정점을 새로운 이동가능한 정점에서 제거하여, 다음 재귀호출을 진행한다. 여기서 이동가능한 정점이 [1, 8]이 존재한다면, for문은 1하고 8을 모두 돌아보게 된다. 1을 돌아 볼 경우에는 dfs로 재귀 호출을 보낼 때, 현재 정점이 1이 되고, 이동가능한 정점이 [8]이 된다. 8을 돌게 되면, 재귀호출 시에 현재 정점이 8이 되고, 이동가능한 정점이 [1]이된다. for문을 역할은 이동가능한 정점을 하나씩 각각 순회하여, 모든 경우의 수를 탐색하는 역할이다. 해당 정점을 순회할 경우 해당 정점이 곧 현재 정점이 되고, 이미 방문을 하였기 때문에 재방문을 하면 곤란하므로 이동가능한 정점에서 자기 자신을 제거 하는 것이 된다. 단방향그래프 이므로, 그럼 같은 정점을 다시 방문하는 일을 만들지 않게 되어, 시간복잡도가 획기적으로 줄게 될 것이다.
수행 5.

결과 변수를 리턴하면 게임 끝....
주의할 점.

이동가능한 정점은 리스트의 형태로 재귀호출을 보낼 경우, 리스트가 완전 복제가 일어나지 않게 되면, 독립적 변수로 취급이 되지 않아 다른 곳에서 값을 바꾸면 연쇄적으로 이어져서 값이 바뀌어 최악의 상황을 초래하게 된다. 항상 배열이나 리스트의 자료형태를
값을 독립적으로 바꾸는 작업을 수행 할 때는, 무조건 복제를 하여 독립적 리스트로써 사용하도록 주의해야한다.
분명 말했습니다. 완탐문제에서는 이런 문제가 아주 많이 발생합니다. 주의합시다.

결과 변수의 최대값 갱신은 항상 양과 늑대의 수를 업데이트한 이후와 늑대의 수를 양의 수를 넘었는 지의 조건문을 탐색하는 그 중에 배치해야한다. 가끔 그런 분들이 있을 수 있는데, 당연히 wolf가 sheep의 수를 따라잡거나 초과하는 조건문에서만 결과 변수의 최댓값을 갱신하는 분이 있을 수 있다. 하지만 그렇게 되면, 모든 정점을 탐색하는 경우에 양의 수가 늑대의 수보다 많은 경우를 탐색하는 것이 불가능할 것이다. 이런 어이없는 경우가 생기지 않도록 조심하자.

레벨 3치고는 생각보다 어렵지 않은 문제입니다.
오히려 레벨2의 양궁 대회가 더 레벨 3과 같이 느껴집니다.
그래도 자세한 설명을 알고 싶은 여러분들을 위해서 이 글을 작성합니다.
도움이 되셨으면 댓글 부탁합니다. 또한 해설에 논리적인 에러가 보이면 그것도 지적 부탁합니다. """


import copy

answer = 0


def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for e in edges:
        parents, child = e[0], e[1]
        graph[parents].append(child)
    # print(graph)
    node, sheep, wolf = 0, 0, 0
    passable_node = []

    def dfs(node, sheep, wolf, passable_node):
        global answer
        try:
            passable_node_ = copy.deepcopy(passable_node)
            if node in passable_node_:
                passable_node_.pop(passable_node_.index(node))
            if info[node] == 0:
                sheep += 1
            else:
                wolf += 1
            answer = max(answer, sheep)
            # print(node,sheep,wolf,passable_node_)
            if sheep <= wolf:
                return
            for g in graph[node]:
                passable_node_.append(g)
            for p in passable_node_:
                dfs(p, sheep, wolf, passable_node_)
        except:
            pass
            # print("E :", node,sheep,wolf,passable_node)

    dfs(node, sheep, wolf, passable_node)

    return answer
