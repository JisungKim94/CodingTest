def solution(number, k):
    answer = []

    for num in number:
        if not answer:
            answer.append(num)
            continue  # 아래 코드를 실행하지 않고 건너 뜀

        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)

    print(answer)
    answer = answer[:-k] if k > 0 else answer
    print(answer)
    # "_".join(['a','b','c']) : a_b_c 로 변환
    return "".join(answer)


print(solution("1924", 2) == "94")
print(solution("1231234", 3) == "3234")
print(solution("4177252841", 4) == "775841")
print(solution("8999991", 3) == "9999")
