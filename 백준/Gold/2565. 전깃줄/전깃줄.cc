#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(pair<int,int> a, pair<int,int> b)
{
    return a.first < b.first;
}

int main()
{
    int N, max = 0, num, b;
    vector<pair<int,int>> list;

    cin >> N;

    for(int i = 0; i < N ; i++)
    {
        cin >> num;
        cin >> b;
        list.push_back(pair<int,int>(num, b));
    }

    sort(list.begin(), list.end(), compare);

    for(int i = 0; i < N; i++)
    {
        list[i].first = list[i].second;
        list[i].second = 1;
        
        for(int j = 0; j < i; j++)
        {
            if(list[j].first < list[i].first && list[j].second >= list[i].second)
                list[i].second = list[j].second + 1;
        }
        if(list[i].second > max) max = list[i].second;
    }

    cout << N - max;

    return 0;
}