N = int(input())
numbers = list(map(int, input().split()))
# print(numbers)

# 쉬운 구현문제

if N>=2:
    # numbers[0]*a+b = numbers[1]
    # numbers[1]*a+b = numbers[2]
    if N == 2:
        if numbers[1] == numbers[0]:
            print(numbers[0])
        else:
            print("A")
    else:
        if numbers[1]==numbers[0]:
            a,b = 1,0
        else:
            a = (numbers[2]-numbers[1])/(numbers[1]-numbers[0])
            b = numbers[1]-numbers[0]*a
        flag = 0
        # print(a,b)
        for i in range(N-1):
            if numbers[i+1] == numbers[i]*a+b:
                flag = 0
            else:
                flag = 1
                break
        if int(a)==a and int(b)==b:
            pass
        else:
            flag = 1
            
        if flag:
            print("B")
        else:
            print(numbers[-1]*int(a)+int(b))
            
else:
    print("A")
