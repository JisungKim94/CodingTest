# =======================================
# sqrt 구현해서 써보려 했는데 알고리즘은 되는데,
# 자료형이 float이나 double로 나오지가 않네.. 찾아서 해결하자.. 참고로 python에서는 걍 **0.5 쓰면 제곱근이래 eg. 
# a = 2**0.5 = 1.4142....
# def sqrt(input_arg):
#     for i in range(1,30):
#         Retval = 2
#         Retval = (Retval + (input_arg / Retval))/2
#         return Retval
# =======================================

Testcase = int(input())

for _ in range(Testcase):
    x, y = map(int,input().split())
    distance = y - x
    if distance <= 3:
        print(distance)
    else:
        Sqrt = int(distance**0.5)
        if distance == Sqrt ** 2:
            print(2*Sqrt-1)
        elif Sqrt**2 < distance <= Sqrt**2+Sqrt:
            print(2*Sqrt)
        else:
            print(2*Sqrt+1)