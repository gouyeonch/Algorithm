#include <stdio.h>
#include <string.h>

int main()
{
	char word[1000001];
	int i, max = 0, cnt = 0, ind,alp[26] = { 0 };

	scanf("%s", word);

	for (i = 0; word[i]!='\0'; i++)
	{
		if (word[i] >= 'a') alp[word[i] - 'a']++;
		else alp[word[i] - 'A']++;
	}

	for (i = 0; i < 26; i++)
	{
		if (max <= alp[i])
		{
			max = alp[i];
			ind = i;
		}
	}
	for (i = 0; i < 26; i++)
	{
		if (alp[ind] == alp[i]) cnt++;
	}

	if (cnt > 1)putchar('?');
	else printf("%c", ind + 'A');

	return 0;
}