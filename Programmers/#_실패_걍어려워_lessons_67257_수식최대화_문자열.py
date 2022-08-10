from itertools import permutations


def operation(num1, num2, op):
    if op == "+":
        return str(int(num1) + int(num2))
    if op == "-":
        return str(int(num1) - int(num2))
    if op == "*":
        return str(int(num1) * int(num2))


# isdigit 문자가 '단 하나'라도 있다면 False를 반환하고,모든 문자가 '숫자'로만 이루어져있으면 True를 반환합니다.
def calculate(exp, op):
    array = []
    tmp = ""
    # 일단 주어진 문자열을 ['100', '-', '200', ' * ', '300', '-', '500', '+', '20'] 와 같이 만든다. (array)
    for i in exp:
        if i.isdigit() == True:
            tmp += i
        else:
            array.append(tmp)
            array.append(i)
            tmp = ""
    array.append(tmp)

    # 그리고 스택 자료구조를 활용해 해당 연산자를 만났을때 계산함수를 수행한다. 그리고 계속 array를 갱신해간다.
    # stack에는 o in op가 있기 전 까지의 expressions가 담겨있음
    # array에는 o in op가 있은 후 의 expressions가 담겨있다.
    # operation 함수를 지나면 stack에 o in op 전후의 계산값이 담긴다.
    # 핵심은 array에는 expression을 남겨놓고 operation 통과한 뒤 값들을
    # stack에 다시 잘 담아주는건데 쥰내 어렵당..
    for o in op:
        stack = []
        while len(array) != 0:
            tmp = array.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array = stack

    return abs(int(array[0]))


def solution(expression):
    op = ["+", "-", "*"]
    op = list(permutations(op, 3))
    result = []
    for i in op:
        result.append(calculate(expression, i))
    return max(result)


# print(solution("100-200*300-500+20") == 60420)
print(solution("50*6-3*2") == 300)
