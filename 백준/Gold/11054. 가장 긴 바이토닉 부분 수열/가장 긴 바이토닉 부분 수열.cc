//가장 긴 바이토닉 부분수열
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, max = 0, num, sum;
    vector<pair<int,int>> list, sub;

    cin >> N;

    for(int i = 0; i < N; i++)
    {
        cin >> num;
        list.push_back(pair<int,int>(num, 1));

        for(int j = 0; j < i; j++)
        {
            if(list[j].first < list[i].first && list[j].second >= list[i].second)
                list[i].second = list[j].second + 1;
        }
    }
    for(int i = 0; i < N; i++)
    {
        sub.push_back(pair<int,int>(list[N - 1 - i].first, 1));

        for(int j = 0; j < i; j++)
        {
            if(sub[j].first < sub[i].first && sub[j].second >= sub[i].second)
                sub[i].second = sub[j].second + 1;
        }

        sum = list[N - 1 - i].second + sub[i].second - 1;
        if(sum >max) max = sum;
    }

    cout << max;

    return 0;
}