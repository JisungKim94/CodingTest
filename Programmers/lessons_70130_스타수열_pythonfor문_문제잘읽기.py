def solution(a):
    answer = 0
    # 전체 수열은 짝수
    # 부분 집합은 2개씩 나뉘어짐
    # 모든 부분 집합이 공유하는 원소가 있어야 함
    # 모든 부분 집합은 동일한 원소로 구성되면 안됨

    # 전략
    # 교집합이 젤 많은애를 위주로 조건을 잘 걸어주면 댈듯
    giraffe = [0] * len(a)
    for i in a:
        giraffe[i] += 1
    # print(giraffe)

    for i in range(len(giraffe)):
        if giraffe[i] <= answer:
            continue
        temp = 0
        # python에선 for문 내의 idx를 수정한다고 해서 그게 동작하질 않는다.(c와 다름)
        # 즉 for문 내에서 임의로 idx 증가시키고 싶으면 걍 while 쓰자
        # for idx in range(len(a)-1):
        idx = -1
        while idx < len(a) - 2:
            idx += 1
            if a[idx] != a[idx + 1] and ((a[idx] == i) or (a[idx + 1] == i)):
                idx += 1
                temp += 1
        answer = max(temp, answer)

    return answer * 2
