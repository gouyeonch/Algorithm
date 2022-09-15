#include <stdio.h>



int main()
{
	int N, tot = 1;

	scanf("%d", &N);

	while (N > 0)
	{
		tot *= N;
		N--;
	}
	printf("%d", tot);

	return 0;
}