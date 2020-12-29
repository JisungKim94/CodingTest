#include <stdio.h>
/*=========================================================================================================================

다 0으로 해놓고 특정 index일때만 1로 바꿔주는 개념 사용해서 여집합 개념을 구현함

===========================================================================================================================*/
void selfnumber(int n);

int selfnumcheck_buf[10000] = {0,};

int main()
{
    int input = 1u;

    while(true)
    {
        selfnumber(input);
        input = input + 1u;
        if (input>10000)
        {
            break;
        }
    }
    for (int i = 0; i<10000; i++)
    {
        if(selfnumcheck_buf[i] == 0u)
        {printf("%d\n", i);}
    }


}

void selfnumber(int n)
{
    int first = 0;
    int second = 0;
    int third = 0;
    int fourth = 0;
    int sum = 0;
    int output = 0;
    int N = 0u;
    N = n;
    if (n<10)
    {
        first = N;
        sum = first;
        output = sum + n;
    }
    else if (n<100)
    {
        second = (N - N%10)/10;
        first = N%10;
        sum = first + second;
        output = sum + n;
    }
    else if (n<1000)
    {
        third = (N - N%100)/100;
        N = N%100;
        second = (N - N%10)/10;
        first = N%10;
        sum = first + second + third;
        output = sum + n;
    }
    else if (n<10000)
    {   
        fourth = (N -N%1000)/1000;
        N = N%1000;
        third = (N - N%100)/100;
        N = N%100;
        second = (N - N%10)/10;
        first = N%10;
        sum = first + second + third + fourth;
        output = sum + n;
    }
    else
    {
        /* nothing to do */
    }
    selfnumcheck_buf[output] = 1u;
}