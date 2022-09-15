#include <stdio.h>

int main()
{
	int X, cnt = 1, sub = 0, ahr, skajwl;

	scanf("%d", &X);

	while (1)
	{
		sub += cnt;
		if (X <= sub)
		{
			if (cnt % 2 == 0)
			{
				ahr = X - (sub - cnt);
				skajwl = sub - X+1;
			}
			else
			{
				skajwl	= X - (sub - cnt);
				ahr = sub - X+1;
			}
			break;
		}
		cnt++;
	}

	printf("%d/%d", ahr, skajwl);

	return 0;
}