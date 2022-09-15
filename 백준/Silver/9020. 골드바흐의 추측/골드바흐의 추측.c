#include <stdio.h>

int main()
{
	int T, i, j, a[10001] = { 0,1 }, b[10001][3], cnt = 0, n;

	for (i = 2; i < 10000; i++)
		for (j = 2; j*i < 10000; j++)
			a[i*j] = 1;
	for (i = 1; i < 10000; i++)
		if (a[i] == 0)
		{
			a[cnt] = i;
			cnt++;
		}// a[]에 10000이하의 소수 대입 (총cnt개

	for (i = 0; i < 10001; i++) b[i][2] = 10000; // 배열 b[][2](파티션의 차이)을 초기화

	for (i = 0; i < cnt; i++)
		for (j = 0; ((j <= i) && ((a[i] + a[j]) <= 10000)); j++)
		{
			if (b[a[i] + a[j]][2] >= a[i] - a[j])
			{
				b[a[i] + a[j]][0] = a[j];
				b[a[i] + a[j]][1] = a[i];
				b[a[i] + a[j]][2] = a[i] - a[j];
			}

		}//10000이하의 골드바흐 파티션을 저장  b[][0]은 파티션 중 작은 수, b[][1]은 파티션 중 큰 수

	scanf("%d", &T);
	for (i = 0; i < T; i++)
	{
		scanf("%d", &n);
		printf("%d %d\n", b[n][0], b[n][1]);
	}

	return 0;
}
//런타임 오류???