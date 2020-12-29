#include <stdio.h>

int main()
{
    int A, B, V = 0;
    int day = 0;

    scanf("%d%d%d",&A,&B,&V);

    day = (int)((V-A + A-B - 1)/(A-B))+1;
    printf("%d",day);
}