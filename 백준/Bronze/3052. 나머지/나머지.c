#include <stdio.h>

int main()
{
	int i, N[10], ch, cnt = 0, j;

	for (i = 0; i < 10; i++)
	{
		scanf("%d", &N[i]);
		N[i] %= 42;
	}

	for (i = 0; i < 10; i++)
	{
		ch = 0;
		for (j = 0; j < i; j++)
		{
			if (N[i] == N[j]) ch = 1;
		}
		if (ch == 0)cnt++;
	}

	printf("%d", cnt);

	return 0;
}