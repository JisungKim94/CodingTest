person_1 = [1, 2, 3, 4, 5]
person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
answers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
answers = [1, 2, 3, 4, 5]


def solution(answers):
    numbers_of_answer = []
    returnvalue = []
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    # 내 답안(c에 가까움)
    for i in range(len(answers)):
        if person_1[i % len(person_1)] == answers[i]:
            cnt_1 = cnt_1 + 1
        if person_2[i % len(person_2)] == answers[i]:
            cnt_2 = cnt_2 + 1
        if person_3[i % len(person_3)] == answers[i]:
            cnt_3 = cnt_3 + 1
    # 위에 내가 짠 코드랑 기능은 거의 동일하지만
    # enumerate라는 python이 제공하는 좋은 기능을 사용하는 답안
    # enumerate 사용하면 list의 indx와 value를 받아서 사용할 수 있음
    for idx, answer in enumerate(answers):
        if person_1[idx % len(person_1)] == answer:
            cnt_1 = cnt_1 + 1
        if person_2[idx % len(person_2)] == answer:
            cnt_2 = cnt_2 + 1
        if person_3[idx % len(person_3)] == answer:
            cnt_3 = cnt_3 + 1

    numbers_of_answer.append(cnt_1)
    numbers_of_answer.append(cnt_2)
    numbers_of_answer.append(cnt_3)

    for i in range(len(numbers_of_answer)):
        if numbers_of_answer[i] == max(numbers_of_answer):
            returnvalue.append(i + 1)

    return returnvalue
