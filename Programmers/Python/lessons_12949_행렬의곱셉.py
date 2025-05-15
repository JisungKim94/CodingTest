def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    # print(answer)
    temp = 0
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                temp = temp + (arr1[i][k] * arr2[k][j])
                # print(i, j, k)
                # print((arr1[i][k] * arr2[k][j]))
                # print(temp)
            answer[i][j] = temp
            temp = 0
    # print(answer)
    return answer


print(
    solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
    == [[15, 15], [15, 15], [15, 15]]
)
print(
    solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])
    == [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
)
print(
    solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4], [2, 4], [3, 1]])
    == [[22, 22], [36, 28], [29, 20]]
)
