#include <stdio.h>

int main()
{
    long int A, B, C = 0;
    int N = 0;

    scanf("%d %d %d", &A, &B, &C);
    N = (int)(A/(C-B));
    
    if (B<C)
    {
        printf("%d", N+1);
    }
    else
    {
        printf("%d", -1);
    }
    
    
}