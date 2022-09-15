#include <stdio.h>

int main()
{
	int a[3], i, right;

	while (1)
	{
		scanf("%d%d%d", &a[0], &a[1], &a[2]);
		if ((a[0] == 0) && (a[1] == 0) && (a[2] == 0)) break;

		right = 0;
		for (i = 0; i < 3; i++)
		{
			if (a[i % 3] * a[i % 3] + a[(i + 1) % 3] * a[(i + 1) % 3] == a[(i + 2) % 3] * a[(i + 2) % 3]) right = 1;
		}

		if (right == 1)printf("right\n");
		else printf("wrong\n");
	}

	return 0;
}