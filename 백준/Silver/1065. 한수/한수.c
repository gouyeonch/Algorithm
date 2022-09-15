#include <stdio.h>
#include <stdlib.h>

int count(int size, int N);

int main()
{
	int N, *pn, order, cnt = 0;

	scanf("%d", &N);

	while (N > 0)
	{ 
		if (N == 1000) cnt += count(4, N);
		else if (N > 99)cnt += count(3, N);
		else if (N > 9)cnt ++;
		else cnt ++;
		N--;
	}
	printf("%d", cnt);

	return 0;
}
int count(int size, int N)
{
	int *pn, i, ch ;

	pn = (int *)malloc(size*(sizeof(int)));
	if (pn == NULL)
	{
		printf("메모리가 부족합니다!");
		exit(1);
	}

	for (i = 0; i < size; i++)
	{
		ch = 0;
		pn[i] = N % 10;
		N /= 10;
		if ((i > 1) && (pn[i] - pn[i - 1]) == (pn[i - 1] - pn[i - 2])) ch = 1;
	}

	free(pn);

	if (ch == 1) return 1;
	else return 0;	
}
