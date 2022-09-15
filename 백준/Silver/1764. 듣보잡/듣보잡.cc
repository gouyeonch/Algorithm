//듣보잡
#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, M, count = 0;
    set<string> list;
    string name;
    vector<string> nameList;

    cin >> N >> M;

    for(int i = 0; i < N; i++)
    {
        cin >> name;
        list.insert(name);
    }

    for(int i = 0; i < M; i++)
    {
        cin >> name;
        if(list.find(name) != list.end())
        {
            count++;
            nameList.push_back(name);
        }
    }

    sort(nameList.begin(), nameList.end());

    cout << count << endl;
    for(auto i : nameList) 
        cout << i << "\n";

    return 0;
}