T = int(input())
for i in range(0, T, 1):
    a,b = map(int, input().split())
    ans = a + b
    print("Case #%d: %d"%(i+1, ans))