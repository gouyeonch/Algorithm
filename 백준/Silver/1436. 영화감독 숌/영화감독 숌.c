#include <stdio.h>

int main()
{
	int N, n[10001], i = 0 , cnt6 = 0, num = 666, temp;

	scanf("%d", &N);

	while(i!=N)
	{
		temp = num;
		cnt6 = 0;

		while (temp > 0)
		{
			if (temp % 10 == 6)cnt6++;
			else cnt6 = 0;
			
			if (cnt6 == 3)break;
			temp /= 10;
		}

		if (cnt6 == 3)
		{
			i++;
			n[i] = num;
		}
		num++;
	}
	printf("%d", n[N]);

	return 0;
}