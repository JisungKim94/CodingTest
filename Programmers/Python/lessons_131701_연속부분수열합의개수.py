def solution(elements):
    answer = 0
    length = len(elements)
    length2 = length * 2

    elements = elements + elements
    temp = set([])

    for i in range(length):
        i = i + 1
        for j in range(length):
            idxlength = i
            if (j + idxlength) <= (length2 + 1):
                # print(sum(elements[j : j + idxlength]))
                temp.add(sum(elements[j : j + idxlength]))
        # print(temp)
        # print(len(temp))
        # print("idxlength :", idxlength)
    answer = len(temp)
    return answer


# 내꺼보다 10배 빠른 풀이
# 1) 원형수열의 끝점이 mod로 정해지니까 element 길이를 안 늘려도댐
# 2) 시작점을 정하고 길이가 1,2,3,..인 애를 구함
# 난 길이가 1,2,3,... 인 애들의 시작점을 돌림
# 이건 속도차이에 크게 영향은 없을거 같음...
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i + 1, i + ll):
            print(j, ll, j % ll, elements[j % ll])
            ssum += elements[j % ll]
            res.add(ssum)
    return len(res)


print(solution([7, 9, 1, 1, 4]) == 18)
