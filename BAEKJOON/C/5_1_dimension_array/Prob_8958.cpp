#include <stdio.h>
#include <string.h>

int main()
{
	int N = 0u;
	int Point = 1u;
	char Array[80] = {0, };
    char preArray = 0;
	int length = 0u;
	int sum = 0u;

	scanf("%d", &N);

	for (int i = 0; i < N; i++){
		scanf("%s", &Array);	// scanf_s는 메모리 크기도 input으로 넣어줘야댐
		length = sizeof(Array) / sizeof(char);

		for (int i = 0; i < length; i++){
			if ((Array[i] == 'O')){
				if (Point == 0){
					Point = 1u;
				}
				if (Array[i] == preArray){
					Point = Point + 1u;
				}

			}
			if ((Array[i] == 'X') || (Array[i] == 0)){
				Point = 0u;
			}
			sum = Point + sum;
			preArray = Array[i];
		}
		printf("%d\n", sum);
		sum = 0u;
		Point = 1u;
		preArray = 0;
	}

}