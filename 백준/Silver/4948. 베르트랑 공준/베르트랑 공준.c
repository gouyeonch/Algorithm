#include <stdio.h>

int main()
{
	int n, i, j, cnt = 0, a[246913];

	while (1)
	{
		scanf("%d", &n);
		if (n == 0)break;

		for (i = 0; i <= 246913; i++) a[i] = 0;
		a[1] = 1;

		for (i = 2; i < 2 * n; i++)
			for (j = 2; j*i <= 2*n; j++)
				a[j*i] = 1;
		
		for (i = n+1; i <= 2 * n; i++) if (a[i] == 0)cnt++;

		printf("%d\n", cnt);
		cnt = 0;
	}

	return 0;
}
