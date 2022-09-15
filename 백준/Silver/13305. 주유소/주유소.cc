//주유소
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, num, money = 0,  min = 1000000000;
    vector<int> len;

    cin >> N;

    for(int i = 0; i < N - 1; i++)
    {
        cin >> num;

        len.push_back(num);
    }

    for(int i = 0; i < N - 1; i++)
    {
        cin >> num;

        if(num < min) min = num;

        money += len[i] * min;
    }

    cout << money;

    return 0;
}