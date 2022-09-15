#include <stdio.h>

int main()
{
	int x, y, w, h, loww, lowh;

	scanf("%d%d%d%d", &x, &y, &w, &h);

	if ((w - x) <= x) loww = w - x;
	else loww = x;

	if ((h - y) <= y)lowh = h - y;
	else lowh = y;

	if (loww >= lowh)printf("%d", lowh);
	else printf("%d", loww);

	return 0;
}