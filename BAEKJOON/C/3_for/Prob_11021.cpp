#include <stdio.h>

int main()
{
	long T = 0;
	int a = 0;
	int b = 0;
	int x = 1;

	scanf("%d", &T);

	for (long i = 0; i < T; i++)
	{
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", x, a + b);
		x = x + 1;
	}
    
}