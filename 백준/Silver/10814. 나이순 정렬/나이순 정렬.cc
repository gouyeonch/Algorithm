#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool compare(pair<int, string> a, pair<int, string> b)
{
    return a.first < b.first;
}

int main()
{
    int N, age;
    string name;
    vector<pair<int, string>> list;

    cin >> N;

    for(int i = 0; i < N; i++)
    {
        cin >> age >> name;
        list.push_back(pair<int, string>(age, name));
    }

    stable_sort(list.begin(), list.end(), compare);

    for(int i = 0; i < N; i++)
        cout << list[i].first << " " << list[i].second << "\n";

    return 0;
}