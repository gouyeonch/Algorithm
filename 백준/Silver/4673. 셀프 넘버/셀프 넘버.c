#include <stdio.h>

int d(int n);

int main()
{
	int dnumber[10000], i, j, ch;

	for (i = 0; i < 10000; i++)
	{
		dnumber[i] = d(i + 1);
	}

	for (i = 1; i < 10000; i++)
	{
		ch = 0;
		for (j = 0; j < i; j++)
		{
			if (i == dnumber[j]) ch = 1;
		}
		if (ch == 0) printf("%d\n", i);
	}

	return 0;
}

int d(int n)
{
	int sum = n;

	while (n > 0)
	{
		sum += n%10;
		n /= 10;
	}

	return sum;
}