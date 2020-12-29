#include <stdio.h>

int main()
{
    int N = 0;
    int sum = 0;
    char s[100] = {0,};

    scanf("%d", &N);
    scanf("%s", s);

    for (int i = 0; i <N; i++)
    {
        sum = s[i] + sum - '0'; // 문자열을 받으면 아스키숫자로 저장된다. 0부터 9까지 0x30 0x31 ... 0x39 즉, 얘를 int로 출력하면 저 16진수 수가 나오겠지 근데
                                // '0'을 빼주니까 0부터 9까지 0x00 0x01 ... 0x09 가 되서 0~9가 되는거다. '0'을 빼줘도 되고 걍 숫자 48 (=0x30)해도됨
    }

    printf("%d", sum);

}