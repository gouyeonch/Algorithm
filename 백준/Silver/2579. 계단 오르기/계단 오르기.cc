//계단 오르기
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, num;
    vector<pair<pair<int,int>, pair<int,int>>> dp;
    pair<int, int> p1;
    pair<int, int> p2;

    cin >> N;
    cin >> num;

    p1 = pair<int,int>(0, 0);
    p2 = pair<int,int>(0, 0);
    dp.push_back(pair<pair<int,int>, pair<int,int>>(p1, p2));
    p1 = pair<int,int>(num, 1);
    p2 = pair<int,int>(num, 1);
    dp.push_back(pair<pair<int,int>, pair<int,int>>(p1, p2));

    for(int i = 2; i <= N; i++)
    {
        cin >> num;

        if(dp[i-2].first.first > dp[i-2].second.first) p1 = pair<int,int>(dp[i-2].first.first + num, 1);
        else p1 = pair<int,int>(dp[i-2].second.first + num, 1);

        p2 = pair<int,int>(dp[i-1].first.first + num, 2);

        dp.push_back(pair<pair<int,int>, pair<int,int>>(p1, p2));
    }

    if(dp[N].first.first > dp[N].second.first) cout << dp[N].first.first;
    else cout << dp[N].second.first;

    return 0;
}