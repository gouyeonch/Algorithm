#include <stdio.h>
#include <stdlib.h>

int main()
{
	int T, i;
	int *pA, *pB;

	scanf("%d", &T);
	pA = (int*)malloc(T * sizeof(int));
	pB = (int*)malloc(T * sizeof(int));
	if ((pA == NULL) || (pB == NULL))
	{
		printf("메모리가 부족합니다!");
		exit(1);
	}

	for (i = 0; i < T; i++)
	{
		scanf("%d%d", &(pA[i]), &(pB[i]));
	}

	for (i = 0; i < T; i++)
	{
		printf("Case #%d: %d + %d = %d\n", i + 1, pA[i], pB[i], pA[i] + pB[i]);
	}

	return 0;
}