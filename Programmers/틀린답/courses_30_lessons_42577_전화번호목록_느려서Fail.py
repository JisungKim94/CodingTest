# 이거 효율성에서 통과 못함... 겁나 느린가봉가

phone_book = ["119", "97674223", "1195524421"]  # false
# phone_book = ["123", "456", "789"]  # true
# phone_book = ["12", "123", "1235", "567", "88"]  # false


answer = True
cnt = 0
for i in range(len(phone_book)):
    check_num = phone_book[i]
    for j in range(len(phone_book)):
        k = len(check_num)
        check_num2 = phone_book[j][:k]
        print("check_num :", check_num)
        print("check_num2 :", check_num2, "\n")
        if check_num == check_num2:
            cnt = cnt + 1
    if cnt > len(phone_book):
        answer = False
    else:
        answer = True


print(answer)
print(cnt)
