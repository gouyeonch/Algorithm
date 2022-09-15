#include <stdio.h>

int main()
{
	int pnt[3][2], x = 0, y = 0 , i, j;

	scanf("%d%d%d%d%d%d",&pnt[0][0], &pnt[0][1], &pnt[1][0], &pnt[1][1], &pnt[2][0], &pnt[2][1]);

	if (pnt[0][0] == pnt[1][0])x = pnt[2][0];
	else if (pnt[0][0] == pnt[2][0])x = pnt[1][0];
	else x = pnt[0][0];
	if (pnt[0][1] == pnt[1][1])y = pnt[2][1];
	else if (pnt[0][1] == pnt[2][1])y = pnt[1][1];
	else y = pnt[0][1];

	printf("%d %d", x, y);

	return 0;
}