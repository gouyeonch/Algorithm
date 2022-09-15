#include <stdio.h>

int main()
{
	int T, k, n, i, j;
	int ary[15][15], cnt = 0;
	
	for (i = 0; i < 15; i++)
	{

		ary[0][i] = cnt;
		cnt++;
	}
	for (i = 0; i < 15; i++)
	{
		ary[i][1] = 1;
	}
	for (i = 1; i < 15; i++)
	{
		for (j = 2; j < 15; j++)
		{
			ary[i][j] = ary[i - 1][j] + ary[i][j - 1];
		}
	}

	scanf("%d", &T);

	for (i = 0; i < T; i++)
	{
		scanf("%d%d", &k, &n);
		printf("%d\n", ary[k][n]);
	}

	return 0;
}