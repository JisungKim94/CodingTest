import collections


def main():
    answer = 0
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                visited[i][j] = 2
    # d : 0,북 1,동 2,남 3,서
    stack = collections.deque([(r, c, d)])
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while stack:
        cr, cc, cd = stack.popleft()
        if visited[cr][cc] == 0:
            stack.append((cr, cc, cd))
            visited[cr][cc] = 1
            continue
        # print(cr, cc, cd)
        # for i in visited:
        #   # print(i)
        flag = 0
        for i in range(1, 5):
            nd = (cd - i) % 4
            nr, nc = cr + move[nd][0], cc + move[nd][1]
            # print(nr, nc, nd)
            # print(visited[nr][nc] == 0, board[nr][nc] == 0)
            if 0 <= nr <= N and 0 <= nc <= M:
                if visited[nr][nc] == 0 and board[nr][nc] == 0:
                    flag = 1
                    stack.append((nr, nc, nd))
                    break
        if flag == 0:
            # print("f=0", cr, cc, cd)
            if cd == 0:
                nr, nc = cr - move[cd][0], cc - move[cd][1]
            elif cd == 1:
                nr, nc = cr - move[cd][0], cc - move[cd][1]
            elif cd == 2:
                nr, nc = cr - move[cd][0], cc - move[cd][1]
            else:
                nr, nc = cr - move[cd][0], cc - move[cd][1]
            # print("f=0", nr, nc, cd)
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 0:
                    stack.append((nr, nc, cd))
                else:
                    break
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                answer += 1
    print(answer)


if __name__ == "__main__":
    main()
