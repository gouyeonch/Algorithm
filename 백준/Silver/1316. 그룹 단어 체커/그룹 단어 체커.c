#include <stdio.h>

int main()
{
	char word[101];
	int N, i, alpi[26] = { 0 }, j, cnt, k, ch;

	scanf("%d", &N);
	cnt = N;

	for (i = 0; i < N; i++)
	{
		scanf("%s", word);
		getchar();

		for (j = 0; j<26 ; j++)
		{
			ch = 1;
			for (k = 0; word[k] != '\0'; k++)
			{
				if ((word[k] == word[j])&&(ch==1))
				{
					alpi[word[j] - 'a'] = k;
					ch = 2;
				}
				else if ((word[k] == word[j]) && (ch == 2))
				{
					if ((k - alpi[word[j] - 'a']) > 1)
					{
						cnt--;
						ch = 3;
						break;
					}
					else alpi[word[j] - 'a'] = k;
				}
			}
			if (ch == 3)break;
		}
	}

	printf("%d", cnt);

	return 0;
}