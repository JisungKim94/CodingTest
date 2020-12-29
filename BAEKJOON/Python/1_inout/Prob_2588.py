a,b = map(int, input().split())

# a1 = a%10                 # 2
# a10 = (a%100 - a1)/10     # 7
# a100 = (a%1000 - a10)/100 # 4

b1 = b%10                 # 5
b10 = (int)((b%100 - b1)/10)     # 8
b100 = (int)((b%1000 - b%100)/100) # 3

print(b1*a)
print(b10*a)
print(b100*a)
print(b*a)
