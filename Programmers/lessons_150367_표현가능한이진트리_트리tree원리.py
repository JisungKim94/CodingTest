def search(number):
    length = len(number)
    # 내 자식노드가 다 0이거나 다 1이면 그만 찾아도 된다. 잡기술
    if (length == 1) or ("1" not in number) or ("0" not in number):
        return True

    # mid = root노드의 위치
    mid = length // 2
    if number[mid] == "0":
        return False

    # 왼쪽과 오른쪽에 재귀로 탐색을 하고 양쪽 모두 만족해야 함
    return search(number[:mid]) and search(number[mid + 1 :])


def solution(numbers):
    answer = []
    for n in numbers:
        temp = bin(n)[2:]
        p = 0
        while len(temp) > 2**p - 1:
            p += 1
        while len(temp) != 2**p - 1:
            temp = "0" + temp
        if search(temp):
            answer.append(1)
        else:
            answer.append(0)
    return answer
