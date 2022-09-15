#include <stdio.h>

int main()
{
	int i = 0, cnt = 0;
	char alp[16];

	scanf("%s", alp);

	do
	{
		if (alp[i] == 'A') cnt += 3;
		else if (alp[i] == 'B') cnt += 3;
		else if (alp[i] == 'C') cnt += 3;
		else if (alp[i] =='D') cnt += 4;
		else if (alp[i] == 'E' ) cnt += 4;
		else if (alp[i] == 'F') cnt += 4;
		else if (alp[i] == 'G') cnt += 5;
		else if (alp[i] ==  'I') cnt += 5;
		else if (alp[i] ==  'H' ) cnt += 5;
		else if (alp[i] == 'J') cnt += 6;
		else if (alp[i] == 'K' ) cnt += 6;
		else if (alp[i] == 'L') cnt += 6;
		else if (alp[i] == 'M') cnt += 7;
		else if (alp[i] ==  'N' ) cnt += 7;
		else if (alp[i] ==  'O') cnt += 7;
		else if (alp[i] == 'P') cnt += 8;
		else if (alp[i] ==  'Q' ) cnt += 8;
		else if (alp[i] ==  'R' ) cnt += 8;
		else if (alp[i] ==  'S') cnt += 8;
		else if (alp[i] == 'T') cnt += 9;
		else if (alp[i] == 'U' ) cnt += 9;
		else if (alp[i] ==  'V') cnt += 9;
		else cnt += 10;

		i++;
	} while (alp[i] != '\0');

	printf("%d", cnt);

	return 0;
}