#include <stdio.h>



int main()
{   
    int N = 0;
    int output = 0;
    int i_100 = 0;
    int i_10 = 0;
    int i_1 = 0;

    scanf("%d", &N);

    if (N <= 99)
    {
        output = N;
    }
    else
    {  
        for (int i = 100; i <N+1; i++)
        {
                i_100   = (int)(i/100);
                i_10    = (i%100 - i%100%10)/10;
                i_1     = i%10; 
                if ((i_100 - i_10) == (i_10 - i_1))
                {
                    output = output + 1;
                }
        }
    }
    if (N>=100)
    {
        printf("%d",output+99);
    }
    else
    {
        {printf("%d", output);}
    }
}