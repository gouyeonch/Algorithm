#include <stdio.h>

int main()
{
	int M, N, i, j, ch = 0 , tot = 0, n;

	scanf("%d%d", &M, &N);

	for (i = M; i <= N; i++)
	{
		n = 0;
		for (j = 1; j <= i; j++)
		{
			if (i % j == 0) n++;
		}
		
		if ((i != 1) && (n < 3))
		{
			tot += i;
			if (ch == 0) ch = i;
		}
	}
	if (ch == 0)printf("-1");
	else printf("%d\n%d", tot, ch);

	return 0;
}

