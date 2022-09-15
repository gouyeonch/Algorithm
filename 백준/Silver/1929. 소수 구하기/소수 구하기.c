#include <stdio.h>

int a[1000001] = { 0,1 };

int main()
{
	int M, N , i, j;

	scanf("%d%d", &M, &N);

	for (i = 2; i < N; i++)
	{
		for (j = 2; j*i <= N; j++)
		{
			a[j*i] = 1;
		}
	}
	for (i = M; i <= N; i++)
	{
		if (a[i] == 0)printf("%d\n", i);
	}

	return 0;
}