//연속합
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, num, dp, max;

    cin >> N;

    cin >> num;
    max = dp = num;
    

    for(int i = 1; i < N; i++)
    {
        cin >> num;
        
        if(dp > 0) num += dp;

        dp = num;

        if(dp > max) max = dp;
    }

    cout << max;

    return 0;
}