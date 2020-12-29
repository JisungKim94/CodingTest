A, B, C = map(int,(input().split()))

D = A*B*C
D = list(str(D))

for i in range(0, 10 ,1):
    print(D.count(str(i)))