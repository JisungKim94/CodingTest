#include <stdio.h>

long long SQRT(long long arg1);

int main()
{
    /* Nothing to do */
}

long long SQRT(long long arg1)
{
    long long X = 2;
    for(int i = 0; i < 10; i++)
    {
        X = ( X + ( arg1 / X ) ) / 2;
    }
    return X;    
}