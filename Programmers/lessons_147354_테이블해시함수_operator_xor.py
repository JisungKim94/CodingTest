import operator

# operator라는 모듈이 있구나~


def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    answer = 0
    for i in range(row_begin - 1, row_end):
        summation = 0
        for j in range(len(data[0])):
            # print(i,j)
            summation = summation + data[i][j] % (i + 1)
        answer = operator.xor(answer, summation)
    return answer
