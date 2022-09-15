#include <stdio.h>
#include <math.h>

double s(double x1, double y1, double x2, double y2);

int main()
{
	int x1, x2, y1, y2, r1, r2, T, tmp, res;
	double d;

	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{
		scanf("%d%d%d%d%d%d", &x1, &y1, &r1, &x2, &y2, &r2);
		d = sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));

		if (d == 0)
		{
			if (r1 == r2)res = -1;
			else res = 0;
		}
		else
		{
			if (r1 < r2)
			{
				tmp = r1;
				r1 = r2;
				r2 = tmp;
			}
			if (((r1 + r2) > d) && ((r1 - r2) < d))res = 2;
			else if (((r1 + r2) == d) || ((r1 - r2) == d))res = 1;
			else res = 0;
		}
		printf("%d\n", res);
	}


	return 0;
}