#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> dp;
    vector<int> tempDp;
    int N, num, temp, max = 0;

    cin >> N;

    cin >> num;
    dp.push_back(num);
    tempDp.push_back(num);

    for(int i = 1; i < N; i++)
    {
        cin >> num;
        tempDp[0] += num;

        for(int j = 1; j < i; j++)
        {
            cin >> num;

            if(dp[j-1] > dp [j]) tempDp[j] = dp[j-1] + num;
            else tempDp[j] += num;
        }

        cin >> num;
        tempDp.push_back(dp[i-1] + num);

        dp = tempDp;
    }

    for(auto n : dp)
        if(n > max) max = n;

    cout << max;

    return 0;
}