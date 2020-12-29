#include <stdio.h>

int main()
{
    long int N = 0;
    int i = 0;
    int sum_i = 0;
    int j = 1;
    int sum_j = 1;
    scanf("%d", &N);

    while (1)
    {
        if (N==1)
        {
            printf("1");
            break;
        }
        else if (N<=7)
        {
            printf("2");
            break;
        }
        else if ((2 + 6*sum_i <= N) && (N <= 1 + 6*(sum_j)))
        {
            printf("%d", i+2);
            break;
        }
        else
        {
            i = i + 1;
            j = j + 1;
            sum_i = sum_i + i;
            sum_j = sum_j + j;
        }
    }
}