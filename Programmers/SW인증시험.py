def solution(files, loss):
    answer = []
    files_dict = {}
    temp = {}
    for i, v in enumerate(files):
        files_dict[i + 1] = v
        temp[i + 1] = 0

    filecnt = 0
    index = 1
    cnt = -1
    keyindex = 0
    tempkeys = list(temp.keys())
    while temp:
        cnt = cnt + 1
        filecnt = filecnt + 1
        print(files_dict, temp)
        if filecnt > files_dict[index]:
            filecnt = 1
            if index == tempkeys[-1]:
                keyindex = 0
                cnt = cnt % loss
                for j in tempkeys:
                    files_dict[j] = files_dict[j] - temp[j]
                    temp[j] = 0
                    if files_dict[j] == 0:
                        answer.append(j)
                        del temp[j]
                tempkeys = list(temp.keys())
                if len(temp) <= 0:
                    break
                index = tempkeys[keyindex]
            else:
                tempkeys = list(temp.keys())
                keyindex = keyindex + 1
                index = tempkeys[keyindex]

        print(files_dict, temp, index)
        if cnt % loss == loss - 1:
            pass
        else:
            temp[index] = temp[index] + 1
    print(answer)
    return answer


# 0000 00000 00 000 0000
# 1101 10110 11 011 0110
# 1111 11110 11 111 1110
# 1111 11111 11 111 1111
print(solution([4, 5, 2, 3, 4], 3) == [3, 1, 4, 2, 5])
print(solution([3, 2, 3, 4], 2) == [1, 2, 4, 3])
print(solution([5, 5, 5, 5, 5], 31) == [1, 2, 3, 4, 5])
