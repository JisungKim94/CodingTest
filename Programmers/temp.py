temp = ""
arry = []
for i in "100-200*300-500+20":
    if i.isdigit():
        temp = temp + i
    else:
        arry.append(temp)
        arry.append(i)
        temp = ""

print(arry)
