def solution(n, k, cmds):
    answer = ""
    deleted = []
    datas = {}
    # datas는 idx마다 [pre, data, next, 삭제여부] 로 이루어져있다.
    for i in range(n):
        datas[i] = datas.get(i, []) + [i - 1, i, i + 1, 1]
    datas[0][0] = None
    datas[n - 1][2] = None

    try:
        for cmd in cmds:
            cmd = cmd.split(" ")
            if cmd[0] == "U":
                for _ in range(int(cmd[1])):
                    k = datas[k][0]
            elif cmd[0] == "D":
                for _ in range(int(cmd[1])):
                    k = datas[k][2]
            elif cmd[0] == "C":
                deleted.append(k)
                datas[k][3] = 0
                if datas[k][2] == None:
                    datas[datas[k][0]][2] = None
                    k = datas[k][0]
                elif datas[k][0] == None:
                    datas[datas[k][2]][0] = None
                    k = datas[k][2]
                else:
                    datas[datas[k][0]][2] = datas[datas[k][2]][1]
                    datas[datas[k][2]][0] = datas[datas[k][0]][1]
                    k = datas[k][2]
            else:
                temp = deleted.pop()
                datas[temp][3] = 1
                if datas[temp][2] == None:
                    datas[datas[temp][0]][2] = datas[temp][1]
                elif datas[temp][0] == None:
                    datas[datas[temp][2]][0] = datas[temp][1]
                else:
                    datas[datas[temp][2]][0] = datas[temp][1]
                    datas[datas[temp][0]][2] = datas[temp][1]
            # print(k,datas)
    except:
        print("err")

    for i in range(n):
        if datas[i][3] == 1:
            answer = answer + "O"
        else:
            answer = answer + "X"
    return answer
