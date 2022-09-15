#include <stdio.h>
#include <stdlib.h>

int main()
{
	int N, X, i;
	int *pA;

	scanf("%d%d", &N, &X);

	pA = (int *)malloc(N * sizeof(int));
	if (pA == NULL)
	{
		printf("메모리가 부족합니다!");
		exit(1);
	}

	for (i = 0; i < N; i++)
	{
		scanf("%d", &pA[i]);
	}

	for (i = 0; i < N; i++)
	{
		if (pA[i] < X) printf("%d ", pA[i]);
	}

	free(pA);

	return 0;
}