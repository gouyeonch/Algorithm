#include <stdio.h>

int main()
{
	int H, M, clock;

	scanf("%d%d", &H, &M);

	clock = (M + H * 60);

	if (clock>44)
	{
		clock -= 45;

		H = clock / 60;
		M = clock % 60;

		printf("%d %d", H, M);
	}
	else
	{
		clock = 24 * 60 - (45 - clock);

		H = clock / 60;
		M = clock % 60;

		printf("%d %d", H, M);
	}
	

	return 0;
}