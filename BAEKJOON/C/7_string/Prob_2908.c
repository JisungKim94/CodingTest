#include <stdio.h>

int main()
{
    char a[4] = {0,};
    char b[4] = {0,};

    int i, j = 0;

    scanf("%s, %s", a, b);
    for (i = 2; i>=0; i--)
    {
        if (a[i] < b[i])
        {
            for (j = 2; j>=0; j--)
            printf("%c", b[j]);
            break;
        }
        else if (b[j]<a[j])
        {
            for(j=2; j>=0; j--)
            printf("%c", a[j]);
            break;
        }
    }
}
