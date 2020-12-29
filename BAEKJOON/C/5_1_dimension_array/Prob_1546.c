#include <stdio.h>

int main()
{
	int num = 0;
	float Array[1000] = { 0, };
	float max = 0, avg = 0;
	int temp = 0;
	scanf("%d", &num);
	
	for (int i = 0; i < num; i++) 
	{
		scanf("%f", &Array[i]);
		//Array[i] = scanf_s("%f", &temp); // 이렇게 하면 안되는 이유는, scanf_s 가 Array에 저장되는 모양이라서 1,0이 저장되지 temp가 저장되는게 아님
		if (max < Array[i])
			max = Array[i];
	}

	for (int i = 0; i < num; i++) 
	{
		Array[i] = Array[i] / max * 100.0;
		avg += Array[i];
	}

	printf("%.2lf", (avg / (double)num));
}
