#include <stdio.h>

int main()
{
	int N, i, ch = 0, j, cnt = 0, contin, sum;
	char OX[80];

	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		scanf("%s", OX);
		cnt = 0;
		while (OX[cnt] != '\0')
		{
			cnt++;
		}
		contin = 0;
		sum = 0;
		for (j = 0; j < cnt; j++)
		{
			if ((j > 0) && (OX[j] == OX[j - 1])) contin++;
			else contin = 1;
			if(OX[j]=='O') sum += contin;
		}
		printf("%d\n", sum);
	}

	return 0;
}