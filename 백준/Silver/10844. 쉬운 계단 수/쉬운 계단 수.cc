#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    long long dp[10], copyDp[10], sum = 0;

    cin >> N;

    for(auto &n : dp) n = 1;
    copy(dp, dp + 10, copyDp);

    for(int i = 1; i < N; i++)
    {
        dp[0] = copyDp[1];
        dp[9] = copyDp[8];

        for(int j = 1; j <= 8; j++) dp[j] = copyDp[j-1] + copyDp[j+1];

        for(int j = 0; j <= 9; j++) copyDp[j] = dp[j] % 1000000000;
    }

    for(int i = 1; i <= 9; i++) sum += dp[i]%1000000000;

    cout << sum%1000000000;

    return 0;
}