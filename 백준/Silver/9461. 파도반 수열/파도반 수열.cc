//파도반 수열
#include <iostream>

using namespace std;

int main()
{
    int N, c;
    long long ary[101];

    cin >> N;

    ary[0] = 1;
    ary[1] = 1;
    ary[2] = 1;
    ary[3] = 1;
    ary[4] = 2;
    ary[5] = 2;

    for(int i = 0; i < N; i++)
    {
        cin >> c;
        for(int j = 6; j <= c; j++)
        {
            ary[j] = ary[j-1] + ary[j-5];
        }
        cout << ary[c] << endl;
    }

    return 0;
}