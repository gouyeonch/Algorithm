#include <stdio.h>

int main()
{
	int N, cnt = 1, hou = 0;

	scanf("%d", &N);

	while (1)
	{
		cnt += 6 * hou;
		if (N <= cnt)break;
		hou++;
	}
	printf("%d", hou + 1);
	 
	return 0;
}