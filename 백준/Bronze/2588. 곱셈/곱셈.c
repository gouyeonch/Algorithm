#include <stdio.h>

int main()
{
	int first, second;
	int h, d, o;

	scanf("%d", &first);
	scanf("%d", &second);

	h = second / 100;
	d = (second % 100) / 10;
	o = (second % 10);

	printf("%d\n%d\n%d\n%d", first*o, first*d, first*h, first*second);

	return 0;
}