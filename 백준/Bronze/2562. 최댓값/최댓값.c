#include <stdio.h>

int main()
{
	int N[9], i, max=0, index;

	for (i = 0; i < 9; i++)
	{
		scanf("%d", &N[i]);
		if (N[i] > max)
		{
			max = N[i];
			index = i;
		}
	}
	printf("%d\n%d", max, index + 1);

	return 0;
}