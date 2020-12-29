#include <stdio.h>
/*=======================================

array index에 array가 쓰이는 특이한 뇨속 

=========================================*/

int main()
{
    int A = 0;
    int B = 0; 
    int C = 0;
    int D = 0; 
    int a = 0;
    
    int count[10] = {0,};
    int buf[10] = {0,};
    scanf("%d %d %d", &A, &B, &C);
    D = A*B*C;
    
    for (int i = 0; a == 0; i++)
    {
        buf[i] = D%10;
        count[buf[i]] = count[buf[i]] +1;   // 이부분
        D = (int)(D/10);

        if (D == 0)
        {
            a = 1;
        }
        
    }   
    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", count[i]);
    }
    


}
