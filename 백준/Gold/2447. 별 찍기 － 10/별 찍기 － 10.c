#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define size 3000

char star[size][size];

int main()
{
	int N, i, j, cnt, k, l, ch;

	scanf("%d", &N);
	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++) star[i][j] = '*';
	cnt = sqrt(N);

	for (k = 1; k <= cnt; k++)
	{
		ch = pow(3, k);
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < N; j++)
			{
				if (ch / 3 <= i%ch && i%ch < 2 * ch / 3 && ch / 3 <= j%ch && j%ch < 2 * ch / 3)
					star[i][j] = ' ';
			}
		}
	}

	for (i = 0; i < N; i++)
	{
		for (j = 0; j < N; j++)
		{
			printf("%c", star[i][j]);
		}
		putchar('\n');
	}

	return 0;
}
//시간초과