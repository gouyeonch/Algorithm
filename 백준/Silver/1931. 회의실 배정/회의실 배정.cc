//회의실
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, start, fin;
    vector<pair<int, int>> list;
    vector<pair<int, int>> sol;

    cin >> N;

    for(int i = 0; i < N; i++)
    {
        cin >> start >> fin;
        list.push_back(pair<int, int>(fin, start));
    }

    sort(list.begin(), list.end());

    sol.push_back(list[0]);

    for(int i = 1; i < N; i++)
    {
        if(list[i].second >= sol.back().first) sol.push_back(list[i]);
    }

    cout << sol.size() << endl;

    return 0;
}