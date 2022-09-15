#include <stdio.h>

int main()
{
	int i, j, T, cnt = 0, n, num;
	scanf("%d", &T);

	for (i = 0; i < T; i++)
	{
		n = 0;
		scanf("%d", &num);
		for (j = 1; j <= num; j++)
		{
			if (num % j == 0) n++;
		}

		if ((num!=1)&&(n < 3))cnt++;
	}

	printf("%d", cnt);

	return 0;
}