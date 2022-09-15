//1로 만들기
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, num;
    vector<int> dp;

    cin >> N;

    dp.push_back(0);
    dp.push_back(0);
    
    for(int i = 2; i <= N; i++)
    {
        num = i % 6;

        if(num == 0)
        {
            if(dp[i/3] < dp[i/2] && dp[i/3] < dp[i-1]) dp.push_back(dp[i/3] + 1);
            else if(dp[i/2] < dp[i-1]) dp.push_back(dp[i/2] + 1);
            else dp.push_back(dp[i-1] + 1);
        }
        else if(num == 1 || num == 5)
        {
            dp.push_back(dp[i-1] + 1);
        }
        else if(num == 2 || num == 4)
        {
            if(dp[i/2] < dp[i-1]) dp.push_back(dp[i/2] + 1);
            else dp.push_back(dp[i-1] + 1);
        }
        else
        {
            if(dp[i/3] < dp[i-1]) dp.push_back(dp[i/3] + 1);
            else dp.push_back(dp[i-1] + 1);
        }
    }

    cout << dp[N];

    return 0;
}