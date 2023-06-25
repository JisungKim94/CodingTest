# https://davi06000.tistory.com/73
# cases1 의 shallow copy, casses2의 global varible 사용 구현 방법 차이
# quuens 의 deepcopy를 통해 재귀사용 시 단계별 새로운 탐색을 구현하기


cases1 = 0  # global varible of cases


def solution(n):
    global cases1

    def dfs(queens, next_queen):
        # column check
        global cases1
        cases2 = [0]  # shallow copy of the cases (list)

        if next_queen in queens:
            return

        # diagonal check
        for row, column in enumerate(queens):
            h = len(queens) - row
            if next_queen == column + h or next_queen == column - h:
                return

        queens.append(next_queen)
        # end check
        if len(queens) == n:
            cases1 += 1
            cases2[0] += 1
            return

        for next_queen in range(n):
            dfs(queens[:], next_queen)  # deep copy of queens

    for next_queen in range(n):
        queens = []
        dfs(queens, next_queen)
    return cases1
    # return cases2[0]


print(solution(4))
