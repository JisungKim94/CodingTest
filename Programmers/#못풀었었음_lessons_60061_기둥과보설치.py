def solution(n, build_frame):
    answer = []

    def check():
        for ans in answer:
            x, y, bc = ans[0], ans[1], ans[2]
            # 조건 만족 못 할 때만 False 해 줘야하니까 아래처럼 구현
            if bc == 0:
                if (
                    (y == 0)
                    or ((x, y - 1, 0) in answer)
                    or ((x - 1, y, 1) in answer)
                    or ((x, y, 1) in answer)
                ):
                    continue
                return False
            else:
                if (
                    ((x, y - 1, 0) in answer)
                    or ((x + 1, y - 1, 0) in answer)
                    or (((x - 1, y, 1) in answer) and ((x + 1, y, 1) in answer))
                ):
                    continue
                return False
        return True

    for build in build_frame:
        x, y, bc, bd = build[0], build[1], build[2], build[3]
        if bd == 1:
            answer.append((x, y, bc))
            if not check():
                answer.remove((x, y, bc))
        else:
            answer.remove((x, y, bc))
            if not check():
                answer.append((x, y, bc))

    answer.sort()

    return answer
