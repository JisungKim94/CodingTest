import math

# ============================ Class로 구현 ============================
class Calculator:
    def Init(self, x1, y1, r1, x2, y2, r2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.r1 = r1
        self.r2 = r2

    def Distance(self, x1, y1, r1, x2, y2, r2):
        self.result = math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
        return self.result
        
    def subtract(self, r1, r2):
        self.result = r1 - r2 if r1 > r2 else r2 - r1       # python 3항 연산자 (true_return) if (condition) else (false_return)
        return self.result
# ============================ Class로 구현 ============================

test_case = int(input())

for test_case in range(0, test_case, 1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # ============================ Class로 구현 ============================
    Calc = Calculator()
    Calc.Init(x1, y1, r1, x2, y2, r2)
    dist = Calc.Distance(x1, y1, r1, x2, y2, r2)
    subt = Calc.subtract(r1,r2)
    # ============================ Class로 구현 ============================

    if(dist == 0 & r1 == r2):               # 두 원이 완전히 일치하는 경우 
        result = -1
    elif((dist < r1 + r2) & (subt < dist)):   # 두 원의 교점이 2개일 경우 
        result = 2
    elif((dist == r1 + r2) | (dist == subt)):   # 두 원의 교점이 1개일 경우 
        result = 1
    else: result = 0                        # 두 원의 교점이 없을 경우

    print(result, end='\n')

