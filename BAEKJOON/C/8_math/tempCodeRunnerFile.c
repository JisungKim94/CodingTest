#include <stdio.h>

int main()
{
    long int N = 0;
    int i = 0;
    int sum_i = 1;
    int j = 1;
    int sum_j = 1;

    scanf("%d", &N);

    while (1)
    {
        if ((sum_i <= N) && (N <= (sum_j)))
        {
            printf("%d/%d", (sum_j - N + 1),(N - sum_i+1));
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