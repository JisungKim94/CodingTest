import math
# if n is very big number then a[n] will be 2/3;
# lim(a[n]) = 2/3 when n->MAXnumber;
# continued formula, then you will have a[n] := (...)/2^(n-1);
# you must write this with 10^x (x-will be answer);
# like this
# 10^x = 2^(n-1);
# x = lg(2^(n-1))  =>  x = ln(2^(n-1))/ln(10);
N = int(input())
# print(math.log10(2)*(N-1))
# print(math.log10(2)*(N))
n0 = int(math.log10(2) * (N-1))
n1 = int(math.log10(2) * (N))
n2 = int(math.log10(2) * (N+1))
len = n1
if n1==n2 and n1==n0+1 and N%2 !=0:
    len = n0
print(len)