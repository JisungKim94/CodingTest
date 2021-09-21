array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    temp_array = []
    for temp_commands in commands:
        temp_array = array[temp_commands[0] - 1 : temp_commands[1]]
        temp_array = sorted(temp_array)
        answer.append(temp_array[temp_commands[2] - 1])

    return answer


print(solution(array, commands))
