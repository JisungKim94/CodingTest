a = set([1, 2, 3])
b = range(1,3)
c = [1, 2, 3]
d = list([1, 2, 3])
e = str(113)
print(a)
# print(a(2))   # Error
# print(a[2])   # Error
print("a done")
print(b)
# print(b(2))   # Error
print(list(b))
print(tuple(b))
print("b done")
print(c)
print(c[2])
print("c done")
print(d)
print(d[2])
print("d done")
print(e)
print(e[1])    # str은 숫자를 문자로 변환하는 애임, 한 칸의 크기가 4bit인지 1byte인지 잘 모르겠지만 여튼 한칸에 한개씩 숫자를 저장한다.
               # 즉 e = 113이므로 str(e) = [1, 1, 3]로 저장된다.
print("e done")
for j in e:   # 그래서 이런식으로 표현하면 j가 1, 1, 3을 print 하게된다.
    print(j)