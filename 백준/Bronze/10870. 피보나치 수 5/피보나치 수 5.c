#include <stdio.h>

int main()
{
	int n[21] = { 0,1 },N;

	scanf("%d", &N);

	for (int i = 2; i <= N; i++)
	{
		n[i] = n[i - 1] + n[i - 2];
	}

	printf("%d", n[N]);
	return 0;
}