def solution(m, n, puddles):
    answer = 0
    grid = [[0] * n for _ in range(m)]
    for i, v in enumerate(grid):
        v[0] = 1
        if i == 0:
            for j in range(len(v)):
                v[j] = 1

    for puddle in puddles:
        for i, v in enumerate(grid):
            if puddle[0] == 1:
                for j, w in enumerate(v):
                    if j >= puddle[1] - 1:
                        v[j] = 0
            if puddle[1] == 1:
                if i >= puddle[0] - 1:
                    v[0] = 0

    for i in range(m):
        for j in range(n):
            if i - 1 >= 0 and j - 1 >= 0:
                grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
                for puddle in puddles:
                    grid[puddle[0] - 1][puddle[1] - 1] = 0
    answer = grid[m - 1][n - 1]
    answer = answer % 1000000007
    # print(grid)
    return answer


# print((solution(4, 3, [[2, 2]]) == 4))
# print((solution(4, 3, [[2, 1], [3, 3]]) == 1))
# print((solution(4, 3, [[2, 1]]) == 4))
# print(solution(2, 2, []) == 2)
# print(solution(3, 3, []) == 6)
# print(solution(3, 3, [[2, 2]]) == 2)
# print(solution(3, 3, [[2, 3]]) == 3)
# print(solution(3, 3, [[1, 3]]) == 5)
# print(solution(3, 3, [[1, 3], [3, 1]]) == 4)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]) == 2)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]) == 1)
# print(solution(4, 4, [[3, 2], [2, 4]]) == 7)
# print(solution(100, 100, []) == 690285631)
# print(
#     solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]])
#     == 0
# )  # 이 값이 잘 나오면 테스트1, 테스트9 통과, 위로 가면 안됨
print((solution(4, 3, [[1, 2], [2, 1]]) == 0))

""" dp방식으로 푸시면 대부분
첫 행과, 첫 열에 전부 1를 부여하여 경로를 체크할 겁니다.
하지만, 이 문제가 dp를 이용하여 풀어야 한다는 점과,
아래하고 오른쪽으로 밖에 이동할 수 없다는 점이 존재하기 때문에,
생기는 문제가 있습니다.
장애물로는 완벽히 막히지는 않았지만, 못가는 경우가 존재하는 케이스가 있습니다.
장애물 때문에 아래로 내려다가 오른쪽으로 이동하는데 그 부분에
같은 높이의 장애물이 존재한다면, 이번판은 망한겁니다.
왜냐하면, 위로 다시 올라 가는 경우는 존재하지 않기 때문입니다.
모든 장애물의 위치마다 조건을 걸어주는 것은 약간 좀 귀찮아보입니다.
조금만 더 머리를 굴려봅시다.
값을 부여하는 부분부터 잘 부여하면, 방법은 그대로 가되, 위로 역류하는 부분을 방지할 수 있는
방법이 존재합니다.
다른 방식으로 생각해보면, 첫 행과 첫 열에 장애물이 존재하지 않는다면,
역류하는 경우가 생길 까요? 그렇죠? 안생깁니다.
그럼 첫 행과, 첫 열에 1을 부여 할 때, 장애물이 존재하기 직전까지만 1을 부여하는 겁니다.
그럼 장애물 이후에 있는 부분들은 0값을 가지게 되므로 계산을 하더라도 0가지의 길이 계산됩니다.
그럼 자연스럽게 역류하는 방법의 길의 경우의 수는 계산되지 않습니다.
애초부터 1을 부여 할때, 첫 행과 첫 열에 장애물이 있으면, 그 아래나, 우측은 갈 수 있는 방법이 없기 때문에,
1을 부여하지 않는다고, 생각하시면 쉬울 것 같습니다.
왜냐하면 막혀있는 장애물을 넘어서 갈려면 좌측이나 위로 이동해야만 갈 수 있는 부분이기 때문입니다. """
