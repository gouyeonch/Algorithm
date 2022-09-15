//좌표 압축
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare1(pair<int, int> a, pair<int, int> b)
{
    return a.first < b.first;
}

bool compare2(pair<int, int> a, pair<int, int> b)
{
    return a.second < b.second;
}

int main()
{
    int N, X, count = 0, temp = 0;
    vector<pair<int, int>> list;

    cin >> N;

    for(int i = 0; i < N; i++)
    {
        cin >> X;
        list.push_back(pair<int, int>(X, i));
    }

    sort(list.begin(), list.end(), compare1);

    temp = list[0].first;
    list[0].first = count;
    for(int i = 1; i < N; i++)
    {
        if(temp != list[i].first)
        {
            temp = list[i].first;
            count++;
        }
        list[i].first = count;
    }

    sort(list.begin(), list.end(), compare2);

    for(int i = 0 ; i < N ; i++)
        cout << list[i].first << " ";

    return 0;
}