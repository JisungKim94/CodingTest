v = list(range(10))

for i in v:
    if i == 5:
        print(i)
    else:
        print("NO")


print([i if i == 5 else "NO" for i in v])
