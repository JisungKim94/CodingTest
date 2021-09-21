# find() : 문자열 중 처음 str이 위치한 자리 return, 없는 경우 -1 return

# phone_book = ["119", "97674223", "1195524421"]  # false
# phone_book = ["123", "456", "789"]  # true
phone_book = ["12", "0578", "123", "1235", "567", "88"]  # false


def solution(phone_book):
    answer = True

    # sort를 하면 str일 경우에도 "0"이 "1"보다 앞으로 오고 "12"가 "17"보다 앞으로 정렬 되므로
    # 인접한 애들 두 개만 비교해도 된다!!! << for문 한개로만 사용 가능
    phone_book = sorted(phone_book)

    # zip으로 phone_book이랑 phone_book[1:]을 (phone_book, phone_book[1:]) 꼴로 합침
    # 두 list length가 다른데 이럴 경우 짧은걸 기준으로 만들어짐
    # for loop에서 각각 p1(=phone_book), p2(phone_book[1:])로 사용
    # 이렇게 하면 서로 붙어있는 애들 두 개를 비교하는 것 처럼 사용할 수 있음
    # find를 사용해서 p2에 p1이 있는 위치를 return 받는다. 0일 경우 접두사니까 answer = false
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.find(p1) == 0:
            answer = False
            break

    return answer


# zip으로 만든 list 보려면 이렇게 사용해야함
# print(list(zip(phone_book, phone_book[1:])))

print(solution(phone_book))
