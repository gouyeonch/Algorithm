#include <stdio.h>

int main()
{
	int bugger[3], minb = 2000, bb[2], minbb = 2000, i;

	for (i = 0; i < 3; i++)
	{
		scanf("%d", &bugger[i]);
		if (bugger[i] < minb)minb = bugger[i];
	}
	for (i = 0; i < 2; i++)
	{
		scanf("%d", &bb[i]);
		if (bb[i] < minbb)minbb = bb[i];
	}

	printf("%d", minb + minbb-50);

	return 0;
}