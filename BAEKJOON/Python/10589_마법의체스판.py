import sys
input = sys.stdin.readline
n,m = map(int,input().split())
# 2,2 = 2
# 2,3 = 2
# 2,4 = 3
# 2,5 = 3
# 3,5 = 3

# 3,2 = 2
# 3,3 = 2
# 4,4 = 4
# 5,5 = 4
print(n//2+m//2)
for i in range(n):
    if i%2 == 1: 
        print(i+1,1,i+1,m)
for j in range(m):
    if j%2 == 1: 
        print(1,j+1,n,j+1)