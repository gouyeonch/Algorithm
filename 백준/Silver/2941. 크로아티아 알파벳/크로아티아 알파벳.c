#include <stdio.h>
#include <string.h>

int main()
{
	char word[101];
	int i, cnt = 0;

	scanf("%s", word);

	for (i = 0; i<strlen(word); i++)
	{
		cnt++;
		if ((word[i] == 'c') && (word[i + 1] == '=') || (word[i + 1] == '-')) i++;
		else if ((word[i] == 'd') && (word[i + 1] == '-'))i++;
		else if ((word[i] == 'd') && (word[i + 1] == 'z')&&(word[i+2]=='='))i += 2;
		else if ((word[i] == 'l') && (word[i + 1] == 'j'))i++;
		else if ((word[i] == 'n') && (word[i + 1] == 'j'))i++;
		else if ((word[i] == 's') && (word[i + 1] == '='))i++;
		else if ((word[i] == 'z') && (word[i + 1] == '='))i++;
	}

	printf("%d", cnt);

	return 0;
}