#include <stdio.h>

int main()
{
	int N, M, i, j, k, p, cnt, res = 0, min = 100, rcnt;
	char ch[50][50], modi[43][43];

	scanf("%d%d", &N, &M);

	for (i = 0; i < N; i++) scanf("%s", ch[i]);
		
	for (i = 0; i < N - 7; i++)
		for (j = 0; j < M - 7; j++)
		{
			if (ch[i][j] == 'B') cnt = 0;
			else cnt = 1;
			rcnt = 0;

			res = 0;
			for (k = i; k < i + 8; k++)
				for (p = j; p < j + 8; p++)
				{
					if (cnt % 2 == 0 && ch[k][p] != 'B')res++;
					else if (cnt % 2 == 1 && ch[k][p] != 'W')res++;

					rcnt++;
					if (rcnt % 8 == 0)cnt += 2;
					else cnt++;
				}
			if (res > 32)res = 64 - res;
			if (min > res)min = res;
		}

	printf("%d", min);


	return 0;
}