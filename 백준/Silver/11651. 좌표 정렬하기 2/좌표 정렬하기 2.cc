//좌표 정렬하기2
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b)
{
    if(a.second == b.second) return a.first < b.first;
    else return a.second < b.second;
}

int main()
{
    int N, x, y;
    vector< pair<int, int> > list;

    cin >> N;

    for(int i = 0; i < N; i++)
    {
        cin >> x >> y;

        list.push_back(pair<int, int>(x, y));
    }

    sort(list.begin(), list.end(), compare);

    for(int i = 0; i < N; i++)
        cout << list[i].first << " " << list[i].second << "\n";


    return 0;
}