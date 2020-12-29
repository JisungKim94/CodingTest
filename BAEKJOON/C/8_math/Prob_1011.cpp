#include <stdio.h>

//======================================
// 이거 인풋 아웃 풋은 다 맞는데 
// 백준에서 오답뜨네 자꾸
//======================================
#if 0
int main() 
{
    int T = 0;
    unsigned int x, y = 0;      // y 범위가 2^31 까지니까 unsigned 사용해야 함
    scanf("%d", &T);
    unsigned int distance = 0;
    unsigned int n1 = 0;
    int j = 0;
    
    for (int i = 0; i < T; i++) 
    {
        scanf("%u %u", &x, &y); // scanf type %u는 unsigned int
        distance = y - x;

        while (n1 < distance) 
        {
            j = j + 1;
            n1 = n1 + j * 2;
        }
        printf("%d\n", (n1 - distance) < j ? j * 2 : j * 2 - 1);
    }
    return 0;
}
#endif

//======================================
// 얘랑 인풋 아웃풋 같은데 얘는 맞대
//======================================
int main() {
    int T;
    unsigned int x, y;
    scanf("%d", &T);
    unsigned int sub;
    unsigned int n1;
    unsigned int n2;
    int j;

    for (int i = 0; i < T; i++) {
        scanf("%u %u", &x, &y);
        sub = y - x;
        n1 = 0; n2 = 0; j = 0;
        while (n1 < sub) {
            n2 += j * 2;
            n1 += ++j * 2;
        }
        printf("%d\n", n1 - sub < j ? j * 2 : j * 2 - 1);
    }
    return 0;
}
