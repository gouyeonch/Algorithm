#include <stdio.h>
#include <string.h>

int main()
{
	char index[27], word[100];
	int i;

	for (i = 0; i < 26; i++) index[i] = -1;

	scanf("%s", word);

	for (i = 0; i < strlen(word); i++)
	{
		if(index[word[i] - 'a']  ==-1)index[word[i] - 'a'] = i;
	}

	for (i = 0; i < 26; i++)
	{
		printf("%d ", index[i]);
	}

	return 0;
}