#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    int N, num;
    int list[10001];

    cin.tie(NULL);
    ios::sync_with_stdio(false);

    memset(list, 0, sizeof(list));

    cin >> N;

    for(int i = 0 ; i < N ; i++)
    {
        cin >> num;
        list[num]++;
    }

    for(int i = 1 ; i <= 10000 ; i++)
    {
        for(int j = 0 ; j < list[i] ; j++)
        {
            cout << i << "\n";
        }
    }

    return 0;
}