# https://davi06000.tistory.com/73
# cases 의 shallow copy, global varible 사용
# quuens 의 deepcopy를 통해 재귀사용 시 단계별 새로운 탐색을 구현하기


cases = 0  # global varible of cases


def solution(n):
    global cases

    def dfs(queens, next_queen):
        # column check
        global cases
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
            cases += 1
            cases2[0] += 1
            return

        for next_queen in range(n):
            dfs(queens[:], next_queen)  # deep copy of queens

    for next_queen in range(n):
        queens = []
        dfs(queens, next_queen)
    return cases
    # return cases2[0]
