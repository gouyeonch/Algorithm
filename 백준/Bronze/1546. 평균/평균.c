#include <stdio.h>
#include <stdlib.h>

int main()
{
	int N,  i;
	double avg = 0,max=0 ,* pP ;

	scanf("%d", &N);

	pP = (double*)malloc(N * sizeof(double));
	if (pP == NULL)
	{
		printf("메모리가 부족합니다!");
		exit(1);
	}
	
	for (i = 0; i < N; i++)
	{
		scanf("%lf", &pP[i]);
		if (pP[i] > max) max = pP[i];
	}
	for (i = 0; i < N; i++)
	{
		pP[i] =(pP[i]/ max) * 100;
		avg += pP[i];
	}
	printf("%.2lf", avg / N);

	free(pP);

	return 0;
}