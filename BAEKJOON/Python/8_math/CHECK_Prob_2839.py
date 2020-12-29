inp = int(input())
box = 0

while(1):
    if (inp%5 == 0):
        box = box + (int)(inp/5)
        print(box)
        break

    inp = inp - 3
    box = box + 1

    if (inp<0):
        print("-1")
        break