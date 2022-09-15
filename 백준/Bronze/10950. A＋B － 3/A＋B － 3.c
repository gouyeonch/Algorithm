#include <stdio.h>
#include <stdlib.h>

int main()
{
	int T, i;
	int *pA, *pB;

	scanf("%d", &T);

	pA = (int*)malloc(T * sizeof(int));
	pB = (int*)malloc(T * sizeof(int));
	if (pA == NULL)
	{
		printf("메모리가 부족합니다!\n");
		exit(1);
	}
	if (pB == NULL)
	{
		printf("메모리가 부족합니다!\n");
		exit(1);
	}

	for (i = 0; i < T; i++)
	{
		scanf("%d%d", &pA[i], &pB[i]);
	}

	for (i = 0; i < T; i++)
	{
		printf("%d\n", pA[i]+pB[i]);
	}

	free(pA);
	free(pB);


	return 0;
}