#include <iostream>
#include <vector>

#define MOD 15746

using namespace std;

int main()
{
    int N;
    vector<int> til;

    cin >> N;

    til.push_back(1);
    til.push_back(1);

    for(int i = 2; i <= N; i++)
    {
        til.push_back((til[i-1] + til[i-2])% MOD);
    }

    cout << til[N];

    return 0;
}