T = 0
H = 0
W = 0
N = 0
row = 0
column = 0
T = int(input())

for i in range (0,T,1):
    H, W, N = map(int,input().split())

    row = int(N/H + 1)
    column = int(N%H)
    column = column * 100
    if (column == 0):
        column = H * 100
        row = int(N/H)
    
    print(column+row)