def solution(board):
    answer = 0
    curnode = (0, ((0, 0), (0, 1)))
    rotate_h = [
        ((1, 0, 0, 0), (0, 1, 0, 0)),
        ((-1, 0, 0, 0), (0, 1, 0, 0)),
        ((0, 0, 1, 0), (0, 0, 0, -1)),
        ((0, 0, -1, 0), (0, 0, 0, -1)),
    ]
    rotate_v = [
        ((0, 0, 0, -1), (0, 0, -1, 0)),
        ((0, 0, 0, 1), (0, 0, -1, 0)),
        ((0, 1, 0, 0), (1, 0, 0, 0)),
        ((0, -1, 0, 0), (1, 0, 0, 0)),
    ]
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    N = len(board)
    visited = set([((0, 0), (0, 1))])
    stack = []
    stack.append(curnode)
    while stack:
        ccost, cnodes = stack.pop()
        # print(cnodes)
        (cnode1row, cnode1col), (cnode2row, cnode2col) = cnodes
        if (cnode1row, cnode1col) == (N, N) or (cnode2row, cnode2col) == (N, N):
            return ccost

        for r, c in move:
            nnode1row, nnode1col, nnode2row, nnode2col = (
                cnode1row + r,
                cnode1col + c,
                cnode2row + r,
                cnode2col + c,
            )
            if (
                0 <= nnode1row < N
                and 0 <= nnode1col < N
                and 0 <= nnode2row < N
                and 0 <= nnode2col < N
            ) and (
                board[nnode1row][nnode1col] == 0 and board[nnode2row][nnode2col] == 0
            ):
                if ((nnode1row, nnode1col), (nnode2row, nnode2col)) not in visited:
                    stack.append(
                        (ccost + 1, ((nnode1row, nnode1col), (nnode2row, nnode2col)))
                    )
                    visited.add(((nnode1row, nnode1col), (nnode2row, nnode2col)))

        if cnode1row == cnode2row:
            for x in rotate_h:
                flag = 1
                for r1, c1, r2, c2 in x:
                    nnode1row, nnode1col, nnode2row, nnode2col = (
                        cnode1row + r1,
                        cnode1col + c1,
                        cnode2row + r2,
                        cnode2col + c2,
                    )
                    if (
                        0 <= nnode1row < N
                        and 0 <= nnode1col < N
                        and 0 <= nnode2row < N
                        and 0 <= nnode2col < N
                    ) and (
                        board[nnode1row][nnode1col] == 1
                        or board[nnode2row][nnode2col] == 1
                    ):
                        flag = 0
                if (
                    flag == 1
                    and ((nnode1row, nnode1col), (nnode2row, nnode2col)) not in visited
                ):
                    stack.append(
                        (ccost + 1, ((nnode1row, nnode1col), (nnode2row, nnode2col)))
                    )
                    visited.add(((nnode1row, nnode1col), (nnode2row, nnode2col)))

        if cnode1col == cnode2col:
            for x in rotate_v:
                flag = 1
                for r1, c1, r2, c2 in x:
                    nnode1row, nnode1col, nnode2row, nnode2col = (
                        cnode1row + r1,
                        cnode1col + c1,
                        cnode2row + r2,
                        cnode2col + c2,
                    )
                    if (
                        0 <= nnode1row < N
                        and 0 <= nnode1col < N
                        and 0 <= nnode2row < N
                        and 0 <= nnode2col < N
                    ) and (
                        board[nnode1row][nnode1col] == 1
                        or board[nnode2row][nnode2col] == 1
                    ):
                        flag = 0
                if (
                    flag == 1
                    and ((nnode1row, nnode1col), (nnode2row, nnode2col)) not in visited
                ):
                    stack.append(
                        (ccost + 1, ((nnode1row, nnode1col), (nnode2row, nnode2col)))
                    )
                    visited.add(((nnode1row, nnode1col), (nnode2row, nnode2col)))

    return answer


solution(
    [
        [0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 0],
    ]
) == 21
