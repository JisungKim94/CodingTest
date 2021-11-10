def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    print(make_name)
    idx, answer = 0, 0
    while True:
        print("커서 위치 : ", idx)
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) == 0:
            break
        left, right = 1, 1
        while make_name[idx - left] == 0:
            left += 1
        while make_name[idx + right] == 0:
            right += 1

        print("왼쪽, 오른쪽 :", left, right)
        # 표현법 공부
        # left if left < right else right
        # if문 참이면 if왼쪽거(left) else면 else오른쪽거 (right)
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer


print(solution("JAN"))
# solution("JEROEN")
# solution("JAAXAAANA")
# print(solution("ZZAAAZZ"))  # 답은 8 이미 지나간 곳을 다시 지나가는게 더 빠른 경우
