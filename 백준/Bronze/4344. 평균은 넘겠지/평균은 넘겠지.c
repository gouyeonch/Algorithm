#include <stdio.h>
#include <stdlib.h>

int main()
{
	int N, i, j, avg, cnt;
	double *pp, classmember;

	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		scanf("%lf", &classmember);

		pp = (double*)malloc(classmember * sizeof(double));
		if (pp == NULL)
		{
			printf("메모리가 부족합니다!");
			exit(1);
		}
		avg = 0;
		for (j = 0; j < classmember; j++)
		{
			scanf("%lf", &pp[j]);
			avg += pp[j];
		}
		avg /= classmember;
		cnt = 0;
		for (j = 0; j < classmember; j++)
		{
			if (pp[j] > avg)cnt++;
		}
		printf("%.3lf%%\n", cnt/classmember*100);
	}

	free(pp);

	return 0;
}