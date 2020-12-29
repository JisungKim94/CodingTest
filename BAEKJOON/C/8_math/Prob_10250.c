#include <stdio.h>

int main()
{
    int T = 0;
    int H, W, N = 0;
    int row, column = 0;
    scanf("%d", &T);
    for (int i = 0; i<T; i++)
    {
        scanf("%d%d%d",&H, &W, &N);

        row = N/H + 1;
        column = N%H;
        column = column * 100;
        if (column == 0)
        {
            column = H * 100;
            row = N/H;
        }
        printf("%d\n",(column+row));
    }
    
}