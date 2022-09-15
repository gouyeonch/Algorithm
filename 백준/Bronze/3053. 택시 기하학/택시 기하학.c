#include <stdio.h>
#include <math.h>

int main()
{
	int R;

	scanf("%d", &R);

	printf("%lf\n%lf", pow(R, 2)* 3.14159265358979323, pow(R*sqrt(2), 2));

	return 0;
}
