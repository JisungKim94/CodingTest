def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0

    for i, char in enumerate(name):
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)

        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1

        # A가 나올 때 까지 이동했다가 반대로 가야 하는 경우 e.g. "ZZAAAZZ"
        # 이 경우 i만큼 오른쪽으로 갔다가 다시 i만큼 왼쪽으로 가고 A가 나올 때 까지 돌아간다(next).
        min_move = min(min_move, i + i + len(name) - next)
    answer += min_move
    return answer


print(solution("JAN"))
# solution("JEROEN")
# solution("JAAXAAANA")
# print(solution("ZZAAAZZ"))
