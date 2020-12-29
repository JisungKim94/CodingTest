T = int(input())

for _ in range (T):         # _는 딱히 값을 지정할 필요가 없을 때 사용할 수 있다. 예를들어 index가 필요없는 for loop가 그러하다. for _ in range(X) 는 index 없이 X번 돌고 끝남
    K = int(input())
    N = int(input())
    
    People = [i for i in range(1,N+1)]  # 그냥 통으로 외워야 대나...? 이런 표현이 있나봄 
    for _ in range (K):
        for j in range(1,N):
            People[j] = People[j] + People[j-1]

    print(People[-1])       # 요소가 -1인 애는 전체 행렬 길이에서 -1 한거니까 제일 끝을 가리킴
