#include <stdio.h>

int main()
{   
    static int N = 0;
	static int N10 = 0;
	static int N1 = 0;
	static int out = 0;
	static int cycle = 0;
	static bool firstrun = 0;

	scanf("%d", &N);

	if (0 <= N <= 99)
	{
		if (N <= 9)
		{
			N = N * 10;
		}

		while (out != N)
		{
			if (firstrun == 0)
			{
				out = N;
				firstrun = 1;
			}
			N1 = out % 10;
			N10 = out - N1;
			N10 = N10 / 10;

			out = N1 + N10;
			out = N1 * 10 + (out%10);

			cycle = cycle + 1;
		}
	}
	printf("%d", cycle);

}