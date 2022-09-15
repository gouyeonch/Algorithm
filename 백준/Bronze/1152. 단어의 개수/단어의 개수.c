#include <stdio.h>
#include <string.h>

int main()
{
	int i, cnt = 0;
	char str[1000001];

	gets(str);

	for (i = 0; i < strlen(str); i++)
	{
		if (str[i] == ' ') cnt++;
	}

	if (str[0] == ' ') cnt--;
	if (str[strlen(str) - 1] == ' ') cnt--;

	printf("%d", cnt + 1);

	return 0;
}