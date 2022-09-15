#include <stdio.h>

int main()
{
	int i, N, M, temp;

	scanf("%d", &N);

	for (i = 1; i < N; i++)
	{
		temp = i;
		M = 0;
		M += i;
		while (temp > 0)
		{
			M += temp%10;
			temp /= 10;
		}
		if (M == N)
		{
			printf("%d", i);
			break;
		}
	}
	if (M != N)printf("0");
	

	return 0;
}