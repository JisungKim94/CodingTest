#include <stdio.h>

int main()
{
    int k = 0;
    int n = 0;
    int T = 0;
    int temp = 1;
    scanf("%d", &T);

    int array[15][15] = {0,};
    for (int h = 0; h < 15; h ++)
    {
        array[0][h] = temp;
        temp = temp + 1;
    }
    for (int init_i = 0; init_i < 15; init_i ++)
    {
        array[init_i][0] = 1;
    }
    for (int i = 1; i < 15; i++)
    {
        for (int j = 1; j < 15; j++)
        {
            array[i][j] = array[i][j-1] + array[i-1][j];
        }
    }
    for (int Test = 0; Test < T; Test++)
    {   
        scanf("%d", &k); 
        scanf("%d", &n);
        printf("%d\n", array[k][n-1]);
    }


}