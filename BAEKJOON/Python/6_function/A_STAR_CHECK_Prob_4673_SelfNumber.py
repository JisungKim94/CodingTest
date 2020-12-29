# ========================================================================================================================
# str은 숫자를 문자로 변환하는 애임, 한 칸의 크기가 4bit인지 1byte인지 잘 모르겠지만 여튼 한칸에 한개씩 숫자를 저장한다.
# 즉 e = 113이므로 str(e) = [1, 1, 3]로 저장된다.
# 그래서 이런식으로 표현하면 j가 1, 1, 3을 print 하게된다.
# =========================================================================================================================

natural_number_set = set(range(1, 10001)) # set = 집합개념 (밴다이어그램)
generated_number_set= set()

for i in range(1, 10001):           
    for j in str(i):            
        i += int(j)
    generated_number_set.add(i)

self_number_set = natural_number_set - generated_number_set

for i in sorted(self_number_set):
    print(i)