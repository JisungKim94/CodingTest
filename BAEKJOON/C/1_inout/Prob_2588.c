#include <stdio.h>

int main()
{

	int num1 = 0;
	int num2 = 0;
	int b = 0;
	int a = 0;
	int b1 = 0;
	int b10 = 0;
	int b100 = 0;

	scanf("%d %d", &num1, &num2);		//	scanf ¾µ‹š &ÇÊ¿ä

	b = num1;
	a = num2;

	b1 = b % 10;
	b10 = (int)((b % 100 - b1) / 10);
	b100 = (int)((b % 1000 - b % 100) / 100);

	printf("%d %d %d %d\n", b1 * a, b10 * a, b100 * a, b * a);
    
}