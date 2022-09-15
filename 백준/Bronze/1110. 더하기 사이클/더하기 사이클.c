#include <stdio.h>

int main()
{
	int origin, N = 100, ten, one, second, cnt = 0;
	
	scanf("%d", &origin);
	ten = origin / 10; 
	one = origin % 10;
	second = ten + one;
	N = one*10 + second % 10;
	cnt++;

	while (N != origin)
	{
		ten = N / 10;
		one = N % 10;
		second = ten + one;
		N = one*10 + second % 10;
		cnt++;
	}

	printf("%d", cnt);

	return 0;
}
