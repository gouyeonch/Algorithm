#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int N, count = 0, des = 1, sol = 0;
    vector<int> list;

    cin >> N;

    while(N!=0)
    {
        list.push_back(N%10);
        N /= 10;
        count++;
    }

    sort(list.begin(), list.end(), greater<int>());

    for(int i = 0 ; i < count ; i++)
    {
        sol += list[(count-1) - i] * des;
        des *= 10;
    }

    cout << sol << endl;

    return 0;
}