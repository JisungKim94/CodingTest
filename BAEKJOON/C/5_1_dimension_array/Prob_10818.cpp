#include <stdio.h>

int main()
{
    int N = 0;
    int M = 0;
    int i = 0;
    static int temp_max = 0;
    static int temp_min = 0;
    static bool firstrun = 0;

    scanf("%d", &N);
    
    int array[N-1] = {0,};

    while(1)
    {
        scanf("%d", &M);
        if(firstrun==0)
        {
            temp_max = M;
            temp_min = M;
            firstrun = 1;
        }

        if(M>=temp_max)
        {
            temp_max = M;
        }

        if(M<=temp_min)
        {
            temp_min = M;
        }

        if (i>N-2)
        {
            break;
        }
        i = i + 1;

    }
    printf("%d", temp_min);
    printf(" %d", temp_max);
}