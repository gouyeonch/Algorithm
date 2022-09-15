#include <stdio.h>

int prog[2097152][2];

void hanoi(int *n,int tall, int bposit,int aposit,int posit);

int main()
{
	int n[22] = { 0,1 }, i, N;

	scanf("%d", &N);

	for (i = 2; i <= N+1; i++) n[i] = n[i - 1] * 2+1;
	hanoi(n, N, 1, 3,n[N]/2+1);
	
	printf("%d\n", n[N]);
	for (i = 1; i <= n[N]; i++)printf("%d %d\n", prog[i][0], prog[i][1]);

	return 0;
}

void hanoi(int *n,int tall, int bposit, int aposit,int posit)
{
	int term;

	if (tall == 0)return 0;

	prog[posit][0] = bposit;
	prog[posit][1] = aposit;
	
	if (bposit + aposit == 3)term = 3;
	else if (bposit + aposit == 4)term = 2;
	else if (bposit + aposit == 5)term = 1;

	hanoi(n, tall - 1, bposit, term, posit - (n[tall - 1] / 2 + 1));
	hanoi(n, tall - 1, term, aposit, posit + (n[tall - 1] / 2 + 1));
}
