#include <stdio.h>

int main()
{
	int order = 0, A, B, C, cnt, i, ten = 1, *eachN, mul, N[10] = { 0 }, j;

	scanf("%d%d%d", &A, &B, &C);
	mul = A * B*C;

	while (mul >= ten)
	{
		ten *= 10;
		order++;
	}

	eachN = (int*)malloc(order * sizeof(int));
	ten /= 10;

	for (i = 0; i < order; i++)
	{
		eachN[i] = mul / ten;
		mul -= eachN[i]* ten;
		ten /= 10;
		for (j = 0; j < 10; j++)
		{
			if (eachN[i] == j) N[j]++;
		}
	}

	for (i = 0; i < 10; i++)
	{
		printf("%d\n", N[i]);
	}

	return 0;
}