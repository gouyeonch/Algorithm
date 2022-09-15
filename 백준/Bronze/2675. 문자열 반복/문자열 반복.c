#include <stdio.h>
#include <string.h>

int main()
{
	int T, R[1000], i, j, k;
	char S[1000][21];

	scanf("%d", &T);

	for (i = 0; i < T; i++)
	{
		scanf("%d", &R[i]);
		scanf("%s", S[i]);
	}

	for (i = 0; i < T; i++)
	{
		for (j = 0; j < strlen(S[i]); j++)
		{
			for (k = 0; k < R[i]; k++)
			{
				putchar(S[i][j]);
			}
		}
		putchar('\n');
	}

	return 0;
}