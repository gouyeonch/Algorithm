#include <stdio.h>

int main()
{
	char nums[101];
	int N, i, sum = 0;

	scanf("%d", &N);
	
	getchar();

	for (i = 0; i < N; i++)
	{
		scanf("%c", &nums[i]);
		sum += nums[i]-48;
	}

	printf("%d", sum);
	return 0;
}