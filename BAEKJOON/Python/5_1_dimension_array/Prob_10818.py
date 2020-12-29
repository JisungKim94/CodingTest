# C에 비해서 매우매우매우매우매우 강력함

N = int(input())    # 사실 python에서는 필요없는 값인데 C나 이런곳에서 써야되서 문제에 있는듯
M = list(map(int,input().split()))      # M의 length 정해줄 필요 없이 띄어쓰기 input 받은게 M행렬 자체가 된다.
                                        # 일반적으로 list는 행렬이 아니고 다른개념이지만 python에서는 용어상 행렬이라고 보면되는듯...??(맞나)

print('{} {}'.format(min(M),max(M)))