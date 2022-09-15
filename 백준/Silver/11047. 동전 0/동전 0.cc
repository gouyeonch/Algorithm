//동전 0
#include <iostream>
#include <stack>

using namespace std;

int main()
{
    int N, K, num, cnt = 0;
    stack<int> s;

    cin >> N >> K;

    for(int i = 0; i < N; i++)
    {
        cin >> num;
        s.push(num);
    }

    num = 0;
    while(num != K)
    {
        if(K - num < s.top()) s.pop();
        else 
        {
            num += s.top();
            cnt++;
        }
    }

    cout << cnt << endl;

    return 0;
}