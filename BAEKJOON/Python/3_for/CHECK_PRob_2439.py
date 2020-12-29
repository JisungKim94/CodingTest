N = int(input())

for i in range(1, N+1, 1):
    for j in range(1, N+1, 1):
        if (j <= N - i):
            print(" ", end='')
        else:
            print("*", end='')
    print("\n")
    