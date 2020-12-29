#include <stdio.h>
#include <math.h>

int find_location(int x1, int y1, int r1, int x2, int y2, int r2)
{
    int xdistance = 0u;
    int ydistance = 0u;
    float distance = 0u;
    float distance2 = 0u;
    int ret = 0u;

    xdistance = x1-x2;
    ydistance = y1-y2;
    distance = sqrt(xdistance*xdistance + ydistance*ydistance);
    distance2 = r1>r2 ? r1-r2 : r2-r1;  /* 원 안에 원이 있는 경우 판단기준 */
    /* r1 r2 길이가지고 판단 1개 2개 0개 무한개로 판단하기 */
    if ((x1 == x2) && (y1 == y2) && (r1 == r2))
    {
        ret = -1u;
    }
    else 
    {
        if ((distance < r1 + r2) && (distance2 < distance)) { 
            ret = 2u;
            }
        else if ((distance == r1 + r2) || (distance2 == distance)) {
            ret = 1u; 
            }
        else {
            ret = 0u; 
            }
    }
    return ret;
}

int main()
{
    int test_case;
    int x1, y1, r1, x2, y2, r2;
    int ret;

    scanf("%d", &test_case);

    for (int i = 0; i < test_case; i++)
    {
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

        ret = find_location(x1, y1, r1, x2, y2, r2);
        printf("%d\n", ret);
    }
}