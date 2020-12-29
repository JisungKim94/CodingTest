a = int(input())
# input 한개일때는 map, split 사용하면 안댐 

if ((a%4 == 0) & ((a%100 != 0) | (a%400 == 0))):
    print('1')
else:
    print('0')