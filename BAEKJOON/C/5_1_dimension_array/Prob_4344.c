#include <stdio.h>

int main()
{
    int N = 0;
    int sum = 0;
    int array = 0;
    int M = 0;
    float avg = 0.0;
    int num = 0;

    scanf("%d", &N);

    for(int i = 0; i<N; i++)
    {
        scanf("%d", &M);
        int array[M] = {0,};
        sum = 0;

        for(int j = 0; j<M; j++)
        {
            scanf("%d", &array[j]);
            sum = array[j] + sum;
        }
        avg = (float)(sum/(float)M);

        num = 0;
        for(int j = 0; j<M; j++)
        {
            if(avg<array[j])
            num = num + 1;
        }
        printf("%.3f%%\n", ((float)num/(float)M*100));

    }
}