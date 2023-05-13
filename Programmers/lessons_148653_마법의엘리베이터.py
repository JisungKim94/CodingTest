def solution(storey):
    answer = 0
    storey_list = [0]
    for i in str(storey):
        storey_list.append(int(i))

    storey_list.append(0)
    for i, v in enumerate(storey_list):
        if v > 5:
            storey_list[i] = 10 - storey_list[i]
            storey_list[i + 1] = storey_list[i + 1] + 1
        elif v == 5:
            if storey_list[i + 1] == 9:
                storey_list[i] = 6
                storey_list[i + 1] = 0
            if storey_list[i + 1] == 5:
                storey_list[i] = 5
                storey_list[i + 1] = 6
        else:
            pass

    answer = sum(storey_list)

    return answer
