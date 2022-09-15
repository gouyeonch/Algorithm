#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int K, direc, m, ind, max1, max2;
    vector<pair<int,int>> list;

    cin >> K;

    for(int i = 0; i < 6; i++)
    {
        cin >> direc >> m;
        list.push_back(pair<int,int>(direc, m));
    }

    for(int i = 0; i < 6; i++)
    {
        if(list[i%6].first == list[(i+2)%6].first && list[(i+1)%6].first == list[(i+3)%6].first)
            ind = i;
    }

    max1 = max(max(list[0].second, list[2].second), list[4].second);
    max2 = max(max(list[1].second, list[3].second), list[5].second);

    cout << (max1 * max2 - (list[(ind + 1) % 6].second * list[(ind + 2) % 6].second)) * K;


    return 0;
}