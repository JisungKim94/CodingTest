#include <stdio.h>

int main()
{
	int a = 0;
	scanf("%hd", &a);

	if ((a%4 == 0) && ((a%100 != 0) || (a%400 == 0)))
	{
		printf("%d", 0);	
	}
	else
	{
		printf("%d", 0);
	}
    
}