#include <stdio.h>

int main()
{
	int i, j, k, N[101] = { 0 }, M, max = 0;

	scanf("%d%d", &N[0], &M);

	for (i = 1; i <= N[0]; i++) scanf("%d", &N[i]);

	for (i = 1; i <= N[0]; i++)
		for (j = i+1; i < j&&j <= N[0]; j++)
			for (k = j+1; j < k&&k <= N[0]; k++)
			{
				if (N[i] + N[j] + N[k] <= M && N[i] + N[j] + N[k] >= max)max = N[i] + N[j] + N[k];
			}
	printf("%d", max);


	return 0;
}