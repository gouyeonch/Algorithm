#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b)
{
    if(a.first == b.first) return a.second < b.second;
    else return a.first < b.first;
}

int main()
{
    int N, x, y;
    vector< pair<int, int> > list;

    cin >> N;

    for(int i = 0 ; i < N ; i++)
    {
        cin >> x >> y;
        list.push_back(pair<int, int>(x, y));
    }

    sort(list.begin(), list.end(), compare);

    for(int i = 0 ; i < N ; i++)
        cout << list[i].first << " " << list[i].second << "\n";

    return 0;
}