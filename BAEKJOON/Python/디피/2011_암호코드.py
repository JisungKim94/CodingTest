code = input()
# print(code)
pibonaci = [0, 1, 2]
for i in range(3,5000):
    pibonaci.append(pibonaci[i-2]+pibonaci[i-1])
# print(len(pibonaci))
def test():
    answer = 1
    tmp = 0
    stack = []
    for i in range(len(code)-1):
        if code[i+1] == "0":
            stack.append(code[tmp:i])
            stack.append(code[i:i+2])
            tmp = i+2
            continue
        if int(code[i:i+2])>26:
            stack.append(code[tmp:i+1])
            tmp = i+1
        
    stack.append(code[tmp:])
    # print(stack)
    for i in stack:
        if i:
            if i[0]=='0':
                print(0)
                return
            if len(i)>1 and i[1] == '0':
                if i[0] == "1" or i[0] == "2":
                    answer*=pibonaci[1]
                else:
                    print(0)
                    return
            else:
                answer*=pibonaci[len(i)]
    print(answer%1000000)
test()
# 2
# 2
# 1

# 21
# 2 1
# 21
# 2

# 114
# 1 1 4
# 11 4
# 1 14
# 3

# 1114
# 1 1 1 4
# 11 1 4
# 11 14
# 1 11 4
# 1 1 14
# 5

# 21212
# 2 1 2 1 2
# 21 2 1 2
# 21 21 2
# 21 2 12
# 2 12 1 2
# 2 1 21 2
# 2 1 2 12
# 2 12 12
# 8

# 1111111111
# 89