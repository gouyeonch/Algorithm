#include <stdio.h>

int main()
{
	int N, n[1000], i, j, temp, k;

	scanf("%d", &N);

	for (i = 0; i < N; i++)scanf("%d", &n[i]);

	for (i = 1; i < N; i++)
	{
		for (j = 0; j < i; j++)
		{
			temp = 0;
			if (n[i] < n[j])
			{
				for (k = i; k > j; k--)
				{
					temp = n[k - 1];
					n[k - 1] = n[k];
					n[k] = temp;
				}
			}
		}
	}

	for (i = 0; i < N; i++)printf("%d\n", n[i]);

	return 0;
}