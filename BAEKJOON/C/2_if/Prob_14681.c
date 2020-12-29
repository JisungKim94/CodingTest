#include <stdio.h>

int main()
{
    int a = 0;
	int b = 0;
	
	scanf("%d %d", &a, &b);
	
	if (a<0 && b<0)
	{
		printf("%d", 3);
	}
	else if (a<0 && b>0)
	{
		printf("%d", 2);
	}
	else if (a>0 && b<0)
	{
		printf("%d", 4);
	}
	else
	{
		printf("%d", 1);
	}

}